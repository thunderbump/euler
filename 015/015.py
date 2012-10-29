#!/usr/bin/python
"""Finds the number of paths from one corner of a x by y grid to another. I
can't believe I forgot one of the meanings of binomial coefficients..."""

import sys
import math

argc = len(sys.argv)
X = 20
Y = 20
usage = """015.py [X Y]
Finds the number of paths from one corner of a X by Y grid to another. If no X
or Y are given, 20 is assumed for both. I can't believe I forgot one of the
meanings of binomial coefficients..."""

if argc not in (1, 3):
    print(usage)
    sys.exit(1)
if argc == 3:
    try:
        X = int(sys.argv[1])
        Y = int(sys.argv[2])
    except ValueError:
        print(usage)
        print("X and Y must be numbers")
        sys.exit(1)

#Equivilant to the Xth coefficient in (n+1)^(X+Y), which is (X+Y)C(X)...so...:
print(math.factorial(X+Y)/(math.factorial(X)*math.factorial(Y)))
