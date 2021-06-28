from typing import OrderedDict
from normalizer import *
from collections import Counter
from statistics import median
import json
import pandas as pd
from glob import glob


class BinCloneFunctionWise:
    """
    Binclone implementation with detection, saving db function aware.

    Parameters
    --------
    region_window : int

    Number of lines of asm code the detector will be based on. As the main algorithm
    relies on Sliding window algorithm, this will be main key feature of the code.

    SBSize : int

    Number of features to use for database retrieval.

    pecentile : float

    In the paper, median boundaries were generated to create binary feature vectors with
    those boundary conditions. However, removing zero median features were too fragile in some
    cases. Therefore, conditions can be loosened by removing features with top-T% == 0.
    T is the percentile in this case.

    Examples
    --------
    >>> binclone = BinCloneFunctionWise(region_window = 60, SBSize = 10)
    >>> binclone.generate_database(glob('./data/*.txt'), 'db')
    >>> binclone.load_database('db')
    >>> df = binclone.search_query('query.txt')
    """

    def __init__(self, region_window=60, SBSize=20, percentile=0.8):
        self.region_window = region_window
        self.SBSize = SBSize
        self.percentile = percentile
        assert 0.0 < percentile <= 1.0

    def assign_median_boundary(self, asm_files: list) -> None:
        """
        Registers asm median bounds. save as median_bounds.json.
        Input file paths for asm_file sources.
        This is preprocessing stage.

        Parameters
        --------
        asm_files : list
        list of strings, which individual strings contains path to asm file.

        Returns
        --------
        None

        """

        feat_keys = {}
        reg_cnts = 0
        print("Loading Median Boundary Generator")
        for fp in asm_files:
            asm_funcs, asm_names = normalizer_obj_dump(fp)

            for asm, asm_name in list(zip(asm_funcs, asm_names)):

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
            ord_list = sorted(v + [0] * (reg_cnts - len(v)))
            top_k = round(len(ord_list) * self.percentile)
            if ord_list[top_k] == 0:
                continue
            median_bounds[k] = ord_list[top_k]

        print("Done Generating Median Boundaries, writing...")
        print(median_bounds)
        json.dump(median_bounds, open("med_bounds.json", "w"))

    def create_features_per_window(self, asm_files: list, db: str = "db.csv") -> None:
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
        print(len(features_imp))

        file_ptr = []
        for idx, fp in enumerate(asm_files):
            asm_funcs, asm_names = normalizer_obj_dump(fp, start=18)
            print(asm_names)

            for asm, asm_name in list(zip(asm_funcs, asm_names)):

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

                    bin_vec = "".join(list(map(str, reversed(list(bin_vec.values())))))
                    bin_vec = int(bin_vec, 2)

                    file_ptr.append(
                        (asm_name, asm_name.split(">")[1], hashes[0], fp, idx, bin_vec)
                    )

        df = pd.DataFrame(
            file_ptr,
            columns=[
                "function_name",
                "starting_idx",
                "hashval",
                "filepath",
                "idx",
                "bin_vec",
            ],
        )
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
        self.assign_median_boundary(asm_files)
        self.create_features_per_window(asm_files, db)

    def load_database(self, db: str = "db") -> None:
        self.db = pd.read_csv(db)

    def _load_feature(self, asm_lines: list):
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

        bin_vec = "".join(list(map(str, reversed(list(bin_vec.values())))))
        bin_vec = int(bin_vec, 2)
        return hashes[0], bin_vec

    def search_query(self, query_asm_fp: str) -> pd.DataFrame:
        """
        Returns DataFrame with information on matching query
        """

        asm_funcs = normalizer_obj_dump_functionless(query_asm_fp)

        query_asm = asm_funcs  # Assuming input query only has one function.
        print(query_asm)

        hashval, bin_vec = self._load_feature(query_asm[0 : self.region_window])
        print(hashval)
        alls = self.db[self.db["hashval"] == hashval]

        return alls[["filepath", "function_name", "idx"]]


if __name__ == "__main__":

    binclone = BinCloneFunctionWise(region_window=12, SBSize=5, percentile=0.8)
    # binclone.generate_database(glob("./original/*.txt"), db="db.csv")
    binclone.load_database("db.csv")
    df = binclone.search_query("./queries/t100.txt")

    print(df)
