#!/usr/bin/python
"""Computes the product of a pythagorean triplet who's sum is 1000"""

import sys
import math

def find_perfect_squares(max_value):
    squares = []
    index = 1
    while index <= max_value:
        squares.append(index ** 2)
        index += 1
    return squares

possible_squares = find_perfect_squares(1000)

for a in range(1, 1001):
    for b in range(1, 1001 - a):
        c = a ** 2 + b ** 2
        if c in possible_squares:
#            print a, b, math.sqrt(c)
            if a + b + math.sqrt(c) == 1000:
                print a * b * math.sqrt(c)
