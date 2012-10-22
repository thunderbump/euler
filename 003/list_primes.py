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
        max_val = int(sys.argv[1])
    except:
        print(usage)
        print("X must be a number")
        sys.exit(1)

def is_prime(number, prime_list):
    for prime in prime_list:
        if number % prime == 0:
            return False
    return True

primes = []
reference_file = open("primes", 'r')
try:
    for line in reference_file:
        if line[-1] == '\n':
            line = line[:-1]
        if line[-1] == '\r':
            line = line[:-1]
        primes.append(int(line))
    if 2 not in primes:
        primes.insert(0,2)
except:
    print("no primes found")
    primes.append(2)
reference_file.close()


reference_file = open("primes", 'w')
for candidate in range(primes[-1], max_val + 1):
    if is_prime(candidate, primes):
        primes.append(candidate)
for prime in primes:
    reference_file.write("%d\n" % prime)
reference_file.close()

