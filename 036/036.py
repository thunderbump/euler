#!/usr/bin/python
"""Finds numbers lower than a certain that are palindromes in both base 10 and
base 2."""

import sys

usage = """036.py X
Finds numbers lower than X that are palindromes in both base 10 and base 2."""

def is_dbl_palindrome(number):
    base10 = str(number)
    base2 = bin(number)[2:]
    if base10 != base10[::-1]:
        return False
    if base2 != base2[::-1]:
        return False
    return True

if __name__ == "__main__":
    argc = len(sys.argv)
    if argc != 2:
        print(usage)
        sys.exit(1)
    try:
        X = int(sys.argv[1])
    except ValueError:
        print(usage)
        print("X must be numeric")
        sys.exit(1)

    idx = 1
    dbl_palindromes = []
    while idx < X:
        if is_dbl_palindrome(idx):
            dbl_palindromes.append(idx)
        idx += 1
    #for thing in dbl_palindromes:
    #    print thing, bin(thing)
    print(sum(dbl_palindromes))
