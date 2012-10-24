#!/usr/bin/python

import sys

argc = len(sys.argv)
prime_file_loc = "primes"
usage = """004.py X
Prints the smallest positive integer evenly divisible by all numbers 
from 1 to X
Requires a prime file "primes" made from list_primes with primes up to X...i
should fix this but that's for later."""

if argc != 2:
    print(usage)
    sys.exit(1)
try:
    max_test = int(sys.argv[1])
except:
    print(usage)
    print("X must be a number")
    sys.exit(1)

try:
    prime_file = open(prime_file_loc)
    primes = []
    for line in prime_file:
        if line[-1] == '\n':
            line = line[:-1]
        if line[-1] == '\r':
            line = line[:-1]
        prime = int(line)
        if prime <= max_test:
            primes.append(prime)
        else:  
            break
except EOFError:
    print("Use util/list_primes.py to build a database up to ", max_test)
    sys.exit(1)
except IOError, error:
    print(usage)
    print(error)
    sys.exit(1)
except ValueError:
    print("Corrupt prime DB. Use util/list_primes.py to rebuild the database")
    sys.exit(1)

final_multiple = 1
factors = []
for prime in primes:
    for number in range(1, max_test):
        if len(factors) > 0:
            for factor in factors:
                if number % factor == 0:
                    number /= factor
        while number % prime == 0:
            factors.append(prime)
            number /= prime
for factor in factors:
    final_multiple *= factor
print(final_multiple)
