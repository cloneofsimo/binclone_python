from typing import OrderedDict
from normalizer import normalizer

from collections import Counter
from statistics import median
import json
import pandas as pd
from glob import glob


class BinCloneNaive:
    """
    Binclone implementation with naive region-wise detection

    Parameters
    --------
    region_window : int

    Number of lines of asm code the detector will be based on. As the main algorithm
    relies on Sliding window algorithm, this will be main key feature of the code.

    SBSize : int

    Number of features to use for database retrieval.


    Examples
    --------
    >>> binclone = BinCloneNaive(region_window = 60, SBSize = 20)
    >>> binclone.generate_database(glob('./data/*.txt'), 'db')
    >>> binclone.load_database('db')
    >>> df = binclone.search_query('query.txt')
    """

    def __init__(self, region_window=60, SBSize=20):
        self.region_window = region_window
        self.SBSize = SBSize

    def _assign_median_boundary(self, asm_files: list) -> None:
        """
        Registers asm median bounds. save as median_bounds.json.
        Input file paths for asm_file sources.
        This is preprocessing stage.

        Parameters
        --------
        asm_files : list
        list of strings, which individual strings contains path to asm file.
        asm file must be in format of
        ```






        00000000 <query_func>:
        4087ed:	c9                   	leave
        4087ee:	c2 24 00             	ret    0x24
        4087f1:	55                   	push   ebp
        ```
        Notably, code must start at line 7.

        Returns
        --------
        None

        """

        feat_keys = {}
        reg_cnts = 0
        print("Loading Median Boundary Generator")
        for fp in asm_files:
            asm = normalizer(fp)

            for idx in range(len(asm) - self.region_window):
                _asm = []
                for line in asm[idx : idx + self.region_window]:
                    _asm += line

                features_count = Counter(_asm)
                for k, v in features_count.items():
                    if feat_keys.get(k) is None:
                        feat_keys[k] = []
                    else:
                        feat_keys[k].append(v)
                reg_cnts += 1

        median_bounds = {}
        for k, v in feat_keys.items():
            med = median(v + [0] * (reg_cnts - len(v)))
            if med == 0:
                continue
            median_bounds[k] = med

        print("Done Generating Median Boundaries, writing...")
        print(median_bounds)
        json.dump(median_bounds, open("med_bounds.json", "w"))

    def _create_features_per_window(self, asm_files: list, db: str = "db.csv") -> None:
        """
        Create Window Features, Save as Database.

        Parameters
        --------
        asm_files : list

        list of asm_files folders, simillar to assign_median_boundaries

        db : str

        filepath to save the database. Usually ends with .csv

        """

        features_imp = json.load(open("med_bounds.json"))

        file_ptr = []
        for idx, fp in enumerate(asm_files):
            asm = normalizer(fp)

            for idx in range(len(asm) - self.region_window):
                _asm = []
                for line in asm[idx : idx + self.region_window]:
                    _asm += line
                bin_vec = {k: 0 for k in features_imp.keys()}
                features_count = Counter(_asm)
                for k, v in features_imp.items():

                    if features_count[k] > v:
                        bin_vec[k] = 1
                binval = 0
                hashes = []
                for v in list(bin_vec.values())[: self.SBSize]:
                    binval *= 2
                    binval %= 2 ** self.SBSize
                    binval += v

                for v in list(bin_vec.values())[self.SBSize :]:
                    binval *= 2
                    binval %= 2 ** self.SBSize
                    binval += v
                    hashes.append(binval)

                file_ptr.append((hashes[0], fp, idx + 7))

        df = pd.DataFrame(file_ptr, columns=["hashval", "filepath", "idx"])
        print(df.head())
        df.to_csv(db)

    def generate_database(self, asm_files: list, db: str = "db.csv") -> None:
        """
        Simply creates database.

        Parameters
        --------
        asm_files : list

        list of asm_files folders, simillar to assign_median_boundaries

        db : str

        filepath to save the database. Usually ends with .csv

        """
        self._assign_median_boundary(asm_files)
        self._create_features_per_window(asm_files, db)

    def load_database(self, db: str = "db") -> None:
        self.db = pd.read_csv(db)

    def _load_feature(self, asm_lines: list) -> int:
        """
        Private function used to load features for similarity score.
        """
        features_imp = json.load(open("med_bounds.json"))
        _asm = []
        for line in asm_lines:
            _asm += line
        bin_vec = OrderedDict({k: 0 for k in features_imp.keys()})
        features_count = Counter(_asm)
        for k, v in features_imp.items():
            if features_count[k] > v:
                bin_vec[k] = 1
        binval = 0
        hashes = []
        for v in list(bin_vec.values())[: self.SBSize]:
            binval *= 2
            binval %= 2 ** self.SBSize
            binval += v

        for v in list(bin_vec.values())[self.SBSize :]:
            binval *= 2
            binval %= 2 ** self.SBSize
            binval += v
            hashes.append(binval)

        return hashes[0]

    def search_query(self, query_asm_fp: str) -> pd.DataFrame:
        """
        Returns DataFrame with information on matching query
        """
        query_asm = normalizer(query_asm_fp)
        hashval = self._load_feature(query_asm[: self.region_window])
        print(hashval)
        alls = self.db[self.db["hashval"] == hashval]
        return alls[["filepath", "idx"]]


if __name__ == "__main__":

    binclone = BinCloneNaive(region_window=60, SBSize=24)
    binclone.generate_database(["asms/open18_sort.S", "asms/open18_disrupt.S"], "db")
    binclone.load_database("db")
    df = binclone.search_query("query.S")
    print(df)
