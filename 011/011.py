#!/usr/bin/python
"""Calculates the max product of 4 consecutive numbers found horizontally, 
vertically, or diagonally in a grid."""

import sys

argc = len(sys.argv)
data_file_loc = "grid"
usage = """011.py [data_file]
Calculates the max product of 4 consecutive numbers found horizontally, 
vertically, or diagonally in a grid. If no data file is provided, "grid" is
used."""

if argc > 2:
    print(usage)
    sys.exit(1)
if argc == 2:
    data_file_loc = sys.argv[1]

grid = []
try:
    data_file = open(data_file_loc)
    for line in data_file:
        if line[-1] == '\n':
            line = line[:-1]
        if line[-1] == '\r':
            line = line[:-1]
        x_line = []
        for number in line.split(" "):
            x_line.append(int(number))
        grid.append(x_line)
except IOError, error:
    print(usage)
    print(error)
    sys.exit(1)

def product_walk(x_step, y_step, length, data_set):
    if x_step < 0:
        new_data_set = []
        for line in data_set:
            new_line = []
            for x in line[::-1]:
                new_line.append(x)
            new_data_set.append(new_line)
        data_set = new_data_set
        x_step *= -1
    if y_step < 0:
        new_data_set = []
        for line in data_set[::-1]:
            new_data_set.append(line)
        y_step *= -1
            
    x_index = 0
    y_index = 0
    #posthole. first in the list is the current index so there's one less step
    #than the length says
    x_length = x_step * (length - 1)
    y_length = y_step * (length - 1)
    largest_product = 0
    while y_index < len(data_set) - y_length:
        while x_index < len(data_set[0]) - x_length:
            current_product = 1
            for idx in range(0, length):
                current_product *= data_set[y_index + (y_step * idx)][
                                            x_index + (x_step * idx)]
            if current_product > largest_product:
                largest_product = current_product
            x_index += 1
        y_index += 1
        x_index = 0
    return largest_product

print max(product_walk(1, 0, 4, grid),
          product_walk(0, 1, 4, grid),
          product_walk(1, 1, 4, grid),
          product_walk(-1, -1, 4, grid))
