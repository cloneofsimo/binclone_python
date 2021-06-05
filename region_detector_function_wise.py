from typing import OrderedDict
from normalizer import normalizer, normalizer_obj_dump

from collections import Counter
from statistics import median
import json
import pandas as pd
from glob import glob

def assign_median_boundary(asm_files, region_window = 60):
    """
    Registers asm median bounds. save as median_bounds.json.
    Input file paths for asm_file sources.
    This is almost preprocessing stage.
    """
    
    
    feat_keys = {}
    reg_cnts = 0
    print("Loading Median Boundary Generator")
    for fp in asm_files:
        asm_funcs, asm_names = normalizer_obj_dump(fp)

        for asm, asm_name in list(zip(asm_funcs, asm_names)):
        
            for idx in range(len(asm) - region_window):
                _asm = []
                for line in asm[idx : idx + region_window]:
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
    json.dump( median_bounds, open("med_bounds.json", 'w'))
    

def create_features_per_window(asm_files, region_window = 60, SBSize = 18):

    features_imp = json.load(open("med_bounds.json"))

    file_ptr = []
    for idx, fp in enumerate(asm_files):
        asm_funcs, asm_names = normalizer_obj_dump(fp)

        for asm, asm_name in list(zip(asm_funcs, asm_names)):
        
            for idx in range(len(asm) - region_window):
                _asm = []
                for line in asm[idx : idx + region_window]:
                    _asm += line
                bin_vec = {k : 0 for k in features_imp.keys()}
                features_count = Counter(_asm)
                for k, v in features_imp.items():

                    if features_count[k] > v:
                        bin_vec[k] = 1
                binval = 0
                hashes = []
                for v in list(bin_vec.values())[:SBSize]:
                    binval *= 2
                    binval %= 2**SBSize
                    binval += v
                    
                for v in list(bin_vec.values())[SBSize:]:
                    binval *= 2
                    binval %= 2**SBSize
                    binval += v
                    hashes.append(binval)

                bin_vec = int(''.join(list(map(str,bin_vec.values()))), 2)
                
                file_ptr.append((asm_name, hashes[0], fp, idx, bin_vec))

    df = pd.DataFrame(file_ptr, columns= ["function_name", "hashval", "filepath", "idx", "bin_vec"])
    print(df.head())
    df.to_csv("db")
            
            
def load_feature(asm_lines, SBSize = 18):
    features_imp = json.load(open("med_bounds.json"))
    _asm = []
    for line in asm_lines:
        _asm += line
    bin_vec = OrderedDict({k : 0 for k in features_imp.keys()})
    features_count = Counter(_asm)
    for k, v in features_imp.items():
        if features_count[k] > v:
            bin_vec[k] = 1
    binval = 0
    hashes = []
    for v in list(bin_vec.values())[:SBSize]:
        binval *= 2
        binval %= 2**SBSize
        binval += v
        
    for v in list(bin_vec.values())[SBSize:]:
        binval *= 2
        binval %= 2**SBSize
        binval += v
        hashes.append(binval)

    bin_vec = ''.join(list(map(str,bin_vec.values())))
    bin_vec = int(bin_vec, 2)
    return hashes[0], bin_vec


            
def finding_matchings(query_asm_fp, region_window = 60, inexact = True):

    asm_feat_db = pd.read_csv("db")
    asm_funcs, asm_names = normalizer_obj_dump(query_asm_fp)
    print(asm_funcs)
    query_asm = asm_funcs[0] # Assuming input query only has one function.
    #print(query_asm)
    
    hashval, bin_vec = load_feature(query_asm[0:  region_window])
    print(hashval)
    alls = asm_feat_db[asm_feat_db["hashval"] == hashval]
    if inexact:
        alls["bin_vec"] = alls["bin_vec"] ^ hashval
        for idx in range(len(alls)):
            alls['bin_vec'].iloc[idx]= bin(alls['bin_vec'].iloc[idx].astype(int)).count('1') / 20
        print(alls[["filepath", "idx", 'bin_vec']].values)

    

if __name__ == '__main__':
    #assign_median_boundary(['malware.txt'])
    #create_features_per_window(['malware.txt'])

    finding_matchings('query.S')