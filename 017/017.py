#!/usr/bin/python
"""Computes the number of letters in all numbers below a given X"""

import sys

argc = len(sys.argv)
X = 1000
usage = """017.py [X]
Computes the number of letters in all numbers below a given X. If no X given,
1000 is used."""

raw_number = {0:0, 1:3, 2:3, 3:5, 4:4, 5:4, 6:3, 7:5, 8:5, 9:4, 10:3, 11:6, 
              12:6, 13:8, 14:8, 15:7, 16:7, 17:9, 18:8, 19:8}#below 20 irregular
prefixes = {0:0, 1:4, 2:6, 3:6, 4:5, 5:5, 6:5, 7:7, 8:6, 9:6, 100:7, 1000:8}
len_and = 3

if argc > 2:
    print(usage)
    sys.exit(1)
if argc == 2:
    try:
        X = int(sys.argv[1])
    except ValueError:
        print(usage)
        print("X must be a number")
        sys.exit(1)

def number_to_len_word(number):
    size = 0
    #thousands
    if number // 1000 != 0:
        size += raw_number[number // 1000] + prefixes[1000]
        number %= 1000
    #hundreds
    if number // 100 != 0:
        size += raw_number[number // 100] + prefixes[100]
        if number % 100 != 0:
            size += len_and
        number %= 100
    #tens/ones
    if number < 20:
        size += raw_number[number]
    else:
        size += prefixes[number // 10] + raw_number[number % 10]
    return size

print(sum(number_to_len_word(number)for number in range(1, X + 1)))
#print number_to_len_word(X)
