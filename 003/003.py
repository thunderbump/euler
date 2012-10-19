#!/usr/bin/python
"""Makes a list of primes less than a given number"""

import sys

argc = len(sys.argv)
usage = """list_primes.py X
Makes a list of primes less than a given number X"""

if argc != 2:
    print(usage)
    sys.exit(1)
else:
    try:
        max_val = sys.argv[1]
    except:
        print(usage)
        print("X must be a number")
        sys.exit(1)

def is_prime(number, prime_list)
    for prime in prime_list:
        if number % prime == 0:
            return False
    return True

