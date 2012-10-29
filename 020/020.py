#!/usr/bin/python
"""Computes the sum of the digits in X!"""

import sys
from math import factorial

argc = len(sys.argv)
usage = """020.py X
Computes the sum of the digits in X!"""

if argc != 2:
    print(usage)
    sys.exit(1)
try:
    X = int(sys.argv[1])
except ValueError:
    print(usage)
    print("X must be numeric")
    sys.exit(1)

print(sum(int(char) for char in str(factorial(X))))
