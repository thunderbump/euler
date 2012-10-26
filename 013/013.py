#!/usr/bin/python
"""Computes the first 10 digits of sum of numbers given in the data file"""

import sys

argc = len(sys.argv)
usage = """013.py [data file]
Computes the first 10 digits of sum of numbers given in the data file"""
data_file_loc = "data"

if argc > 2:
    print(usage)
    sys.exit(1)
if argc == 2:
    data_file_loc = sys.argv[1]

try:
    data_file = open(data_file_loc)
    data = []
    for line in data_file:
        if line[-1] == '\n':
            line = line[:-1]
        if line[-1] == '\r':
            line = line[:-1]
        data.append(long(line[:12]))
except IOError, error:
    print(usage)
    print(error)
    sys.exit(1)
except ValueError:
    print(usage)
    print("Corrupted data file.")
    sys.exit(1)

print(str(sum(data))[:10])
