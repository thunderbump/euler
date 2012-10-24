#!/usr/bin/python
"""Computes the difference between the sum of the squares, and the square of
the sum of all numbers up to X"""

import sys

argc = len(sys.argv)
usage = """006.py X
Computes the difference between the sum of the squares, and the square of
the sum of all numbers up to X"""

if argc != 2:
    print(usage)
    sys.exit(1)
try:
    max_test = int(sys.argv[1])
except ValueError:
    print(usage)
    print("X must be a number")
    sys.exit(1)

range_set = range(1, max_test + 1)
print(sum(x for x in range_set)**2 - sum(x**2 for x in range_set))
