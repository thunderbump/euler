#!/usr/bin/python
"""Computes all circular primes below a certain number"""

import sys
from list_primes import get_primes_below

argc = len(sys.argv)
usage = """035.py X
Computes all circular primes below 10^X"""

def get_circular(pwr_of_10):
    primes = get_primes_below(10 ** pwr_of_10)
    circular = []
    for prime in primes:
        original = prime
        step = int(''.join([str(prime)[-1:], str(prime)[:-1]]))
        while step != original:
            if step not in primes:
                break
            step = int(''.join([str(prime)[:-1], str(prime)[-1:]]))
#            print step, str(prime)[-1:], str(prime)[:-1], ''.join([str(prime)[-1:], str(prime)[:-1]])
        if step == original:
#            print step, original, "---"
            circular.append(original)
    return circular
        

if __name__ == "__main__":
    if argc != 2:
        print(usage)
        sys.exit(1)
    try:
        X = int(sys.argv[1])
    except ValueError:
        print(usage)
        print("X must be numeric")
        sys.exit(1)

    print(len(get_circular(X)))
