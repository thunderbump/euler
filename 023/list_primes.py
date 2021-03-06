#!/usr/bin/python
"""Makes a list of primes less than a given number"""

import sys
from math import sqrt, ceil

primes = [2, 3]

def is_prime(number, prime_list):
    for prime in prime_list:
        if number % prime == 0:
            return False
    return True

def get_primes_below(number):
    max_val = number + 1
    candidates = {}
    for init_val in range(2, max_val):
        candidates[init_val] = True
    for prime in range(2, max_val):
        if candidates[prime]:
            for power in range(prime, max_val, prime)[1:]:
                candidates[power] = False
    primes = [prime for prime in candidates if candidates[prime] == True]
    return primes
            

def get_primes_below_old(number):
    for candidate in range(primes[-1], number + 1, 2):
        if is_prime(candidate, primes):
            primes.append(candidate)
    return primes

def get_n_primes(number):
    index = primes[-1]
    while len(primes) < number:
        if is_prime(index, primes):
            primes.append(index)
    return primes


if __name__ == "__main__":
    argc = len(sys.argv)
    usage = """list_primes.py [below | total] X
    below: Prints all primes less than a given number X
    total: Prints out the first X primes"""
    below = False
    total = False
    
    if argc != 3:
        print(usage)
        sys.exit(1)
    if sys.argv[1] == "below":
        try:
            max_val = long(sys.argv[2])
            below = True
        except:
            print(usage)
            print("X must be a number")
            sys.exit(1)
    elif sys.argv[1] == "total":
        try:
            max_val = long(sys.argv[2])
            total = True
        except:
            print(usage)
            print("X must be a number")
            sys.exit(1)
    else:
        print(usage)
        sys.exit(1)
    
        

    primes = []
    reference_file = open("primes", 'r')
    try:
        for line in reference_file:
            if line[-1] == '\n':
                line = line[:-1]
            if line[-1] == '\r':
                line = line[:-1]
            primes.append(long(line))
        if 2 not in primes:
            primes.insert(0,2)
    except:
        print("no primes found")
        primes.append(2)
    reference_file.close()
    
    if below:
        reference_file = open("primes", 'w')
        for candidate in range(primes[-1], max_val + 1):
            if is_prime(candidate, primes):
                primes.append(candidate)
        for prime in primes:
            reference_file.write("%d\n" % prime)
        reference_file.close()
        for prime in primes:
            if prime > max_val:
                break
    #        print(prime),
    
    if total:
        reference_file = open("primes", 'w')
        index = primes[-1] + 1
        while len(primes) < max_val + 1:
            if is_prime(index, primes):
                primes.append(index)
            index += 1
        for prime in primes:
            reference_file.write("%d\n" % prime)
        reference_file.close()
        index = 0
        while index < max_val:
    #        print(primes[index]),
            index += 1
