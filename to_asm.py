import random
from subprocess import Popen, PIPE

from tqdm import tqdm
from glob import glob

import json


def __main():
    """
    Not to be exported.
    """

    pbar = tqdm(glob("./sources/*.cpp"))
    for fpath in pbar:
        prob = fpath.split("\\")[-1][:-4]

        pbar.set_description(prob)

        p = Popen(
            [
                "g++",
                "-S",
                fpath,
                "-masm=intel",
                "-o",
                "./asms/" + prob + ".S",
                "-fno-asynchronous-unwind-tables",
                "-fno-dwarf2-cfi-asm",
            ],
            shell=True,
            stdout=PIPE,
            stdin=PIPE,
        )


if __name__ == "__main__":
    __main()