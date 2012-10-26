#!/usr/bin/python
"""Builds a database of all the Collatz sequences below X, and prints the 
starting number for the longest sequence lower than X, along with its length."""


import sys

argc = len(sys.argv)
usage = """014.py X [data file]
Builds a database of all the Collatz sequences below X, and prints the starting
number for the longest sequence lower than X, along with its length."""
data_file_loc = "collatz_db"

if argc not in (2, 3):
    print(usage)
    sys.exit(1)
if argc == 3:
    data_file_loc = sys.argv[2]
try:
    max_trial = int(sys.argv[1])
except ValueError:
    print(usage)
    print("X must be a number")
    sys.exit(1)

sequence_depths = {}
max_depth = (0,0)
try:
    data_file = open(data_file_loc)
    for line in data_file:
        if line[-1] == '\n':
            line = line[:-1]
        if line[-1] == '\r':
            line = line[:-1]
        dict_vals = line.split(',')
        sequence_depths[int(dict_vals[0])] = int(dict_vals[1])
        if int(dict_vals[1]) > max_depth[1]:
            max_depth = (int(dict_vals[0]), int(dict_vals[1]))
    data_file.close()
except IOError, error:
    print(usage)
    print(error)
    sys.exit(1)
except ValueError:
    print(usage)
    print("Corrupted DB.")
    sys.exit(1)

for x in range(1, max_trial + 1):
    current_sequence = []
    while x not in sequence_depths and x != 1:
        current_sequence.append(x)
        if x % 2 == 0:
            x /= 2
        else:
            x = 3*x + 1
    if x in sequence_depths:
        depth_offset = sequence_depths[x]
    else:
        depth_offset = 1
    while len(current_sequence) != 0:
        depth_offset += 1
        current_item = current_sequence.pop()
        sequence_depths[current_item] = depth_offset
        if depth_offset > max_depth[1]:
            max_depth = (current_item, depth_offset)

print max_depth[0], max_depth[1]

try:
    data_file = open(data_file_loc, 'w')
    for key in sequence_depths:
        data_file.write("%d,%d\n" % (key, sequence_depths[key]))
except IOError, error:
    print(error)
    sys.exit(1)
