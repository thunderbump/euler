#!/usr/bin/python
"""Computes the sum of all digits in a power of 2."""

import sys

argc = len(sys.argv)
shift = 2
usage = """016.py [power]
Computes the sum of all digits in a power of 2."""

if argc > 2:
    print(usage)
    sys.exit(1)
if argc == 2:
    try:
        shift = int(sys.argv[1])
    except ValueError:
        print(usage)
        print("Power of 2 must be a number")
        sys.exit(1)

X = 1 << shift
print(sum(int(char) for char in str(X)))
