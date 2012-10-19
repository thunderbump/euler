#!/usr/bin/python
"""Computes the sum of even valued terms of a 1 2 fibonacci sequence under a given value, or under 4 million if no value is given"""

import sys

argc = len(sys.argv)
usage = """002.py [X]
Computes the sum of even valued terms of a 1 2 fibonacci sequence under X, or under 4 million if no value is given"""

if argc > 2:
    print(usage)
    sys.exit(1)
if argc == 2:
    try:
        max_val = int(sys.argv[1])
        if max_val <= 2:
            print(usage)
            print("why this won't work is left as an exercise to the executor")
    except:
        print(usage)
        print("X must be a number")
        sys.exit(1)
else:
    max_val = 4000000

sequence = [1, 2]
next_val = sequence[-1] + sequence[-2]
while next_val < max_val:
    sequence.append(next_val)
    next_val = sequence[-1] + sequence[-2]
evens = []
for val in sequence:
    if val % 2 == 0:
        evens.append(val)
print(sum(evens))
