#!/usr/bin/python
"""Calculates the path with the largest sum of a path from the top of a
triangle to the bottom"""

import sys

argc = len(sys.argv)
data_file_loc = "data"
usage = """018.py [data file]
Calculates the path with the largest sum of a path from the top of a triangle 
to the bottom"""

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
        tmp_ary = []
        for number in line.split(' '):
            try:
                tmp_ary.append(int(number))
            except ValueError:
                print("Corrupt DB")
                sys.exit(1)
        data.append(tmp_ary)
except IOError, error:
    print(usage)
    print(error)
    sys.exit(1)

#mind's funny :P i'm sure everyone starts at the top
line_idx = len(data) - 1
while line_idx > 0:
    num_idx = 0
    while num_idx < len(data[line_idx]) - 1:
        data[line_idx - 1][num_idx] += max(data[line_idx][num_idx], 
                                           data[line_idx][num_idx + 1])
        num_idx += 1
    line_idx -= 1
print(data[0][0])
