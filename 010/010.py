#!/usr/bin/python
"""Computes the sum of all primes below X. Requires a prime db "primes" built
by util/list_primes up to X"""

import sys

argc = len(sys.argv)
usage = """010.py X
Computes the sum of all primes below X. Requires a prime db "primes" built
by util/list_primes up to X"""

if argc != 2:
    print(usage)
    sys.exit(1)
else:
    try:
        max_val = int(sys.argv[1])
    except ValueError:
        print("X must be a number")
        sys.exit(1)

try:
    data_file = open("../util/primes")
    prime_list = []
    for line in data_file:
        if line[-1] == '\n':
            line = line[:-1]
        if line[-1] == '\r':
            line = line[:-1]
        if int(line) > max_val:
            break
        prime_list.append(int(line))
except ValueError:
    print(usage)
    print("X must be a number")
    sys.exit(1)
except IOError:
    print(usage)
    print("DB not found")
    sys.exit(1)

print(sum(prime_list))
