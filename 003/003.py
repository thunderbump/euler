#!/usr/bin/python
"""Prints all prime factors of X using local list of primes "primes" """

import sys

argc = len(sys.argv)
prime_file_loc = "primes"
usage = """003.py X
Prints all prime factors of X using local list of primes "primes" """

if argc != 2:
    print(usage)
    sys.exit(1)
try:
    factee = long(sys.argv[1])
except:
    print(usage)
    print("X must be a number")
    sys.exit(1)

try:
    prime_file = open(prime_file_loc)
except IOError, error:
    print(error)
    sys.exit(1)

try:
    while factee != 1:
        raw_trial_factor = prime_file.readline()
        if raw_trial_factor == "":
            continue
        if raw_trial_factor[-1] == '\n':
            raw_trial_factor = raw_trial_factor[:-1]
        if raw_trial_factor[-1] == '\r':
            raw_trial_factor = raw_trial_factor[:-1]
        trial_factor = long(raw_trial_factor)
        if factee % trial_factor == 0:
            print(trial_factor),
            while factee % trial_factor == 0:
                factee = factee / trial_factor
                
                
  
except EOFError:
    print(factee)
    print("factors exhausted")
except IOError, error:
    print(error)
    sys.exit(1)
