#!/usr/bin/python

import sys

argc = len(sys.argv)
usage = """044.py
Computes the two pentagonal numbers who's sum and difference are both also 
pentagonal where the magnitude of their difference is minimized."""

def pentagonal(max_num, start=[1]):
    idx = len(start)
    nxt = start[-1]
    while nxt < max_num:
        idx += 1
        nxt = (idx * ((3 * idx) - 1)) / 2
        start.append(nxt)
    return start

if __name__ == "__main__":
    if argc > 2:
        print(usage)
        sys.exit(1)

    pset = pentagonal(10000000)
    index = 0
    while index < len(pset):
        for p in pset[index:]:
            if (p + pset[index] in pset) and (abs(p - pset[index]) in pset):
                print p, pset[index], " difference: ", p - pset[index]
        index += 1
