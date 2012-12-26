#!/usr/bin/python

import sys

argc = len(sys.argv)
usage = """048.py
Computes the last 10 digits of the series n^n where 1 <= n <= 1000"""

if __name__ == "__main__":
    if argc > 2:
        print(usage)
        sys.exit(1)

    p = []
    for n in range(1, 1001):
        p.append((n**n)%10000000000)
    print(sum(p)%10000000000)
