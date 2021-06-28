from region_detector_function_wise import *

if __name__ == "__main__":
    region_window = 40
    SBSize = 14

    queries = glob("./queries/t100.txt")

    print(queries)

    asm_feat_db = pd.read_csv("db")

    correct = 0
    fp_tot = 0

    for fp in queries:
        query_asm = normalizer_obj_dump_functionless(fp)
        hashval, bin_vec = load_feature(query_asm[0:region_window], SBSize=SBSize)
        hubos = asm_feat_db[asm_feat_db["hashval"] == hashval]
        hc = hubos.copy(deep=True)

        # print(hubos)

        for idx in hubos.index:
            val = 1 - bin(int(hc["bin_vec"].loc[idx]) ^ bin_vec).count("1") / SBSize
            # print(val)
            hubos.at[idx, "bin_vec"] = val

        ## start_idxs = [int(name.split(">")[1]) for name in hubos["function_name"]]
        # print(start_idx)
        hubos.at[:, "idx"] = hubos["starting_idx"] + hubos["idx"]
        print(hubos[["filepath", "function_name", "idx", "bin_vec"]])
        idx_range = list(hubos["idx"])

        cnt = 1
        for idx, jdx in zip(idx_range[:-1], idx_range[1:]):
            if jdx - idx != 1:
                cnt += 1
        print("Total suggested group : ", cnt)

        # idx_s, idx_e = idx_range[0] + int(start_idx), idx_range[-1] + int(start_idx)

        ## Find ground truth

        alls = open(fp, "r").read().split("\n")
        flag = alls[0].split()[0][:-1]
        print(flag, fp)
        gt = "./database\\" + fp[-7:]
        alls = open(gt, "r").read().split("\n")

        for fidx, line in enumerate(alls):
            if flag in line.split(":")[0]:
                fidx = fidx
                break
        print(fidx)
        hubos = hubos[hubos["filepath"] == gt]
        idx_t = hubos["idx"]
        for gtidx in idx_t:
            if abs(fidx - gtidx) < 10:
                print(fp, "is found, ", cnt - 1, "other ranges were mistakenly set")
                correct += 1
                break
        # print(fp, f"is in range {idx_s}, {idx_e}, true range is ")
        # break
        fp_rate = 1 / cnt
        fp_tot += fp_rate

    print(correct, "were found, outof ", len(queries))
    print(f"Average Precision {100 * fp_tot / len(queries)} :.4f")
