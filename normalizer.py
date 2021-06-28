import json
import re


def normalizer(filepath):
    """
    Normalize ASM rule-based.
    """
    asm_source = open(filepath, "r").read().split("\n")

    norm_groups = json.load(open("norm.json"))
    print(norm_groups.items())
    asms = []
    for line in asm_source[:-1]:
        line = line.replace("\t", " ").strip().split(" ")
        new_lis = []

        for item in line:
            if len(item) == 0:
                continue
            if item[0] == "_" or item[0] == "L" or item.isdigit():
                item = "VAL"
            if item[0] == "[":
                item = "MEM"
            if item[:5] == ".text":
                item = "text"
            if item[:2] == "0x":
                item = "byte"
            if item[0] == '"':
                item = "char"
            for k, v in norm_groups.items():
                for _v in v:
                    item = item.replace(_v, k)
            new_lis.append(item)
        asms.append(new_lis)

    return asms


def normalizer_obj_dump(filepath, start=6):
    """
    Normalize obj_dump file, intel format, with options described in
    norm.json.
    Current method takes O(n) per line, where n is number of normalizing elements,
    more efficient methods can be developed.
    """
    # asm_source = open(filepath, "rb").read()
    # bom = codecs.BOM_UTF16_LE                                      #print dir(codecs) for other encodings
    # assert asm_source.startswith(bom)                           #make sure the encoding is what you expect, otherwise you'll get wrong data
    # asm_source = asm_source[len(bom):]                         #strip away the BOM
    # asm_source = asm_source.decode('utf-16le').split("\n")

    ## Open with codec utf-8

    asm_source = list(
        enumerate(open(filepath, "r", encoding="utf-8").read().split("\n"))
    )

    norm_groups = json.load(open("norm.json"))
    # print(norm_groups.items())

    functions = []
    cur_func = []
    func_names = []
    # print(asm_source)
    for lidx, line in asm_source[start:-1]:
        splts = line.split(" ")
        # print(line)

        if len(line) < 3:
            continue

        if line[0] != " ":
            functions.append(cur_func)
            # print(cur_func)
            # print(line)
            cur_func = []
            func_names.append(splts[1][:-1] + str(lidx))
            continue

        new_lis = []
        splts = line.split(":")
        line = ":".join(splts[1:])[23:]
        line = line.replace("DWORD", "").replace("PTR", "")

        line = line.replace(",", " ").split()
        # print(line)
        for item in line:
            if item[0] == "_" or item[0] == "L" or item.isdigit():
                item = "VAL"
            if item[0] == "[":
                item = "MEM"
            if item[:5] == ".text":
                item = "text"
            if item[:2] == "0x":
                item = "byte"
            if item[0] == '"':
                item = "char"
            if item[:2] in norm_groups["REGSEG"]:
                item = "REGSEG"

            for k, v in norm_groups.items():
                for _v in v:
                    if _v == item:
                        item = k
                    # item = item.replace(_v, k)
            new_lis.append(item)
        cur_func.append(new_lis)

    functions.append(cur_func)
    return functions[1:], func_names


def normalizer_obj_dump_functionless(filepath):
    """
    Normalize obj_dump file, intel format, with options described in
    norm.json.
    Current method takes O(n) per line, where n is number of normalizing elements,
    more efficient methods can be developed.
    """

    asm_source = open(filepath, "r", encoding="utf-8").read().split("\n")

    norm_groups = json.load(open("norm.json"))
    # print(norm_groups.items())

    # print(asm_source)
    asms = []
    for line in asm_source:
        splts = line.split(" ")

        new_lis = []
        splts = line.split(":")
        line = ":".join(splts[1:])[23:]
        line = line.replace("DWORD", "").replace("PTR", "")

        line = line.replace(",", " ").split()
        # print(line)
        for item in line:
            if item[0] == "_" or item[0] == "L" or item.isdigit():
                item = "VAL"
            if item[0] == "[":
                item = "MEM"
            if item[:5] == ".text":
                item = "text"
            if item[:2] == "0x":
                item = "byte"
            if item[0] == '"':
                item = "char"
            if item[:2] in norm_groups["REGSEG"]:
                item = "REGSEG"

            for k, v in norm_groups.items():
                for _v in v:
                    if _v == item:
                        item = k
                    # item = item.replace(_v, k)
            new_lis.append(item)
        asms.append(new_lis)

    return asms


if __name__ == "__main__":
    func, func_names = normalizer_obj_dump("malware.txt")
    print(func_names)
    # print(func)
