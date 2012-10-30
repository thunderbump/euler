#!/usr/bin/python
"""Computes the amount of sundays that fell on the first of the month during
the 20th century"""

import sys

argc = len(sys.argv)
usage = """019.py
Computes the amount of sundays that fell on the first of the month during
the 20th century"""

if argc != 1:
    print(usage)
    sys.exit(1)

month_length = {0:31, 1:28, 2:31, 3:30, 4:31, 5:30, 6:31, 7:31, 8:30, 9:31,
                10:30, 11:31}
sunday = 6

def is_leap_year(year):
    if year % 4 != 0:
        return False
    #2000 was a leap year
    #if year % 100 == 0 and year % 400 != 0:
    #    return False
    return True

#Begin on the 1900-01-01, which was a Monday(day 0) => Sunday when day % 7 = 6
#day's off by one somewhere. Checking when I can later

#1901-01-01 was a Tuesday
day_count = 1
sunday_first = 0
for year in range(1, 101):
    for month in range(0, 12):
        print year, month, day_count % 7, day_count
        if day_count % 7 == sunday:
            sunday_first += 1
        day_count += month_length[month]
        if month == 1 and is_leap_year(year):
            day_count += 1
print(sunday_first)
