#!/usr/bin/python
"""Calculates the sum of all multiples of 3 and 5 below 1000, or other number if it's given."""

import sys

argc = len(sys.argv)
usage = """001.py [X]
Calculates the sum of all multiples of 3 and 5 below 1000, or X if it's given."""

if argc > 2:
    print(usage)
    sys.exit(1)
if argc == 2:
    try:
        end_val = int(sys.argv[1])
    except:
        print(usage)
        print("X must be a natural number")
        sys.exit(1)
else:
    end_val = 1000

mults_of_3 = []
mults_of_5 = []
index_3 = 3
index_5 = 5
while index_3 < end_val:
    mults_of_3.append(index_3)
    index_3 += 3
while index_5 < end_val:
    mults_of_5.append(index_5)
    index_5 += 5
for index in mults_of_5:
    if index in mults_of_3:
        mults_of_5.remove(index)
#print mults_of_3, '\n', mults_of_5
print(sum(mults_of_3) + sum(mults_of_5))
    
