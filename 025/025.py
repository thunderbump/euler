#!/usr/bin/python
"""Computes the first member of a fibonacci sequence to have a certain number
of digits."""

import sys
from fibonacci import fibonacci

argc = len(sys.argv)
usage = """025.py f1 f2 digits
Computes the first member of a fibonacci sequence to have a certain number
of digits."""

if __name__ == "__main__":
    if argc != 4:
        print(usage)
        sys.exit(1)
    try:
        print(len(fibonacci(int(sys.argv[1]), int(sys.argv[2]), 
                            10 ** (int(sys.argv[3]) - 1))) + 1)
    except ValueError:
        print(usage)
        print("arguments must be numeric")
