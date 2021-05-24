import json


def normalizer(filepath, normalizing_level=["functions equiv", "reggen"]):
    """
    Normalize ASM rule-based.
    """
    asm_source = open(filepath, "r").read().split("\n")

    norm_groups = json.load(open('norm.json'))
    print(norm_groups.items())
    asms = []
    for line in asm_source[:-1]:
        line = line.replace("\t", " ").strip().split(" ")
        new_lis = []
        for item in line:
            if item[0] == '_' or item[0] == 'L' or item.isdigit():
                item = 'VAL'
            if item[0] == '[':
                item = 'MEM'
            if item[:5] == '.text':
                item = 'text'
            if item[:2] == '0x':
                item = 'byte'
            if item[0] == '"':
                item = 'char'
            for k, v in norm_groups.items():
                for _v in v:
                    item = item.replace(_v, k)
            new_lis.append(item)
        asms.append(new_lis)
    
    return asms


if __name__ == "__main__":
    normalizer("asms/open18_sort.S")