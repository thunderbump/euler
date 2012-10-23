#!/usr/bin/python
"""Computes the largest palindrome found by multiply two 3 digit numbers"""

import sys

argc = len(sys.argv)
usage = """004.py
Computes the largest palindrome found by multiply two 3 digit numbers
Currently no arguments(of any kind!) are accepted"""
digit = 3
step = 1
max_multiplier = (10 ** digit) - 1
max_not_found = True
largest_found_palindrome = 0

if argc != 1:
    print(usage)
    sys.exit(1)

first_step = max_multiplier ** 2
if str(first_step) == str(first_step)[::-1]:
    print(first_step)
    sys.exit(0)

while(max_not_found):
    range_higher_than_max = False
    for x in range(0, step):
        current_attempt = (max_multiplier - x) * (max_multiplier - step + x)
        if current_attempt > largest_found_palindrome:
            range_higher_than_max = True
            if str(current_attempt) == str(current_attempt)[::-1]:
                largest_found_palindrome = current_attempt
    if not range_higher_than_max:
        max_not_found = False
    step += 1
print largest_found_palindrome
