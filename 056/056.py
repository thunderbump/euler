#!/usr/bin/python

import sys

argc = len(sys.argv)
usage = """056.py
Calculates the largest digital sum of a^b where a, b < 100"""

if __name__ == "__main__":
    if argc > 2:
        print(usage)
        sys.exit(1)
    maxdsum = 0
    for a in range(1, 100):
        for b in range(1, 100):
            dsum = 0
            for x in str(a**b):
                dsum += int(x)
            if dsum > maxdsum:
                maxdsum = dsum
    print(maxdsum)
