#!/usr/bin/python
"""Computes the greatest multiple of five consecutive digits in a given data
file. "data" used if no argument given"""

import sys

argc = len(sys.argv)
data_file_loc = "data"
window_size = 5
usage = """008.py [data file]
Computes the greatest multiple of five consecutive digits in a given data
file. "data" used if no argument given"""

if argc > 2:
    print(usage)
    sys.exit(1)
if argc == 2:
    data_file_loc = sys.argv[1]

number_list = []
try:
    data_file = open(data_file_loc)
    for line in data_file:
        if line[-1] == '\n':
            line = line[:-1]
        if line[-1] == '\r':
            line = line[:-1]
        for char in line:
            number_list.append(int(char))
except ValueError:
    print("corrupt data file, contents must be numeric")
    sys.exit(1)
except IOError, error:
    print(usage)
    print(error)
    sys.exit(1)

index = 0
largest_product = 0
while index < len(number_list) - window_size:
    scratch = 1
    for number in number_list[index:index + window_size]:
        scratch *= number
    if scratch > largest_product:
        largest_product = scratch
    index += 1

print(largest_product)
