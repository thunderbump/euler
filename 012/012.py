#!/usr/bin/python
"""Computes the lowest triangle number who has at least X divisors."""

import sys

argc = len(sys.argv)
prime_file_loc = "../util/primes"
max_divisors = 500
usage = """012.py [X]
Computes the lowest triangle number who has at least X divisors. If no X is
provided, 500 is used."""

if argc > 2:
    print(usage)
    sys.exit(1)
if argc == 2:
    try:
        max_divisors = int(sys.argv[1])
    except ValueError:
        print(usage)
        print("X must be a number")
        sys.exit(1)

try:
    prime_file = open(prime_file_loc)
    primes = []
    for line in prime_file:
        if len(primes) > max_divisors:
            break
        if line[-1] == '\n':
            line = line[:-1]
        if line[-1] == '\r':
            line = line[:-1]
        primes.append(int(line))
except IOError, error:
    print(usage)
    print(error)
    sys.exit(1)
except ValueError:
    print("Corrupt prime database. Remake with util/list_primes.py")

triangle_index = 1
triangle = 1
num_divisors = 0
while num_divisors < max_divisors:
    triangle_index += 1
    triangle += triangle_index
    prime_finder = triangle
    prime_divisors = {}
    for prime in primes:
    #    print prime, prime_finder, prime_finder % prime
        if prime_finder == 1:
            break
        while prime_finder % prime == 0:
    #        print prime, prime_finder
            prime_finder /= prime
            if prime in prime_divisors.keys():
                prime_divisors[prime] += 1
            else:
                prime_divisors[prime] = 1
    num_divisors = 1
    # this is wrong. making index stop after some rounds
    for key in prime_divisors.keys():
        num_divisors *= prime_divisors[key] + 1
    #print prime_divisors, num_divisors, triangle
print(triangle)
