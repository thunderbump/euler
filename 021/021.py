#!/usr/bin/python
"""Computes the sum of all amicable numbers below X"""

import sys
import math

argc = len(sys.argv)
usage = """021.py X
Computes the sum of all amicable numbers below X"""

#function d as described by http://projecteuler.net/problem=21
def d(number, primes):
    """Computes the sum of all divisors of number. Requires a prime list given
       by util/list_primes.py"""
    prime_divisors = {}
    for prime in primes:
        while number % prime == 0:
            if prime in prime_divisors:
                prime_divisors[prime] += 1
            else:
                prime_divisors[prime] = 1
            number /= prime

if argc != 2:
    print(usage)
    sys.exit(1)
if argc == 2:
    try:
        X = int(sys.argv[1])
    except ValueError:
        print(usage)
        print("X must be numeric")
        sys.exit(1)

prime_list = []
try:
    prime_file = open("../util/primes")
    for line in prime_file:
        if line[-1] == '\n':
            line = line[:-1]
        if line[-1] == '\r':
            line = line[:-1]
        next_prime = int(line)
        if next_prime > X:
            break
        prime_list.append(next_prime)
        
except IOError, error:
    print(usage)
    print(error)
    sys.exit(1)

d(X, prime_list)
