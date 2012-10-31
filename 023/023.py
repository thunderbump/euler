#!/usr/bin/python
"""Finds the sum of all numbers that can't be expressed as the sum of abundant
numbers(sum(divisors(X)) > X)"""

import sys
import divisors

argc = len(sys.argv)
usage = """023.py
Finds the sum of all numbers that can't be expressed as the sum of abundant
numbers(sum(divisors(X)) > X)"""

if argc != 1:
    print(usage)
    sys.exit(1)

#for all integers X > 28123, X can be expressed as the sum of abundant numbers
#so end there.
abundant_numbers = []
for X in range(1, 28124):
    if sum(divisors.all_divisors(X)[:-1]) > X:
        abundant_numbers.append(X)
print abundant_numbers
