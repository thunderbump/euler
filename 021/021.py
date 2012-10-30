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
    if number == 1:
        return 1
    if number in primes:
        return 1
    prime_divisors = {}
    for prime in primes:
        while number % prime == 0:
            if prime in prime_divisors:
                prime_divisors[prime] += 1
            else:
                prime_divisors[prime] = 1
            number /= prime
    if number != 1:
        prime_divisors[number] = 1
    all_divisors = [1]
    for prime in prime_divisors.keys():
        appended_list = []
        for divisor in all_divisors:
            for mult in range(1, prime_divisors[prime] + 1):
                appended_list.append((prime ** mult) * divisor)
        for divisor in appended_list:
            all_divisors.append(divisor)
    return sum(all_divisors[:-1])

if argc != 2:
    print(usage)
    sys.exit(1)
if argc == 2:
    try:
        X = int(sys.argv[1])
        max_prime = math.sqrt(X)
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
        if next_prime > max_prime:
            break
        prime_list.append(next_prime)
        
except IOError, error:
    print(usage)
    print(error)
    sys.exit(1)
except ValueError:
    print("Corrupt prime DB")
    sys.exit(1)

amicable_numbers = []
for candidate in range(1, X):
    compliment = d(candidate, prime_list)
    if d(compliment, prime_list) == candidate:
        if candidate == compliment:
            continue
        if candidate not in amicable_numbers:
            amicable_numbers.append(candidate)
        if compliment not in amicable_numbers:
            amicable_numbers.append(compliment)
print(sum(amicable_numbers))
