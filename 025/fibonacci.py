#!/usr/bin/python
"""Computes fibonacci sequences"""

import sys

argc = len(sys.argv)
usage = """fibonacci.py f1 f2 max_fibonacci_val
Computes the fibonacci sequence starting with f1 and f2 up to the first value
greater than max_fibonacci_val"""

def fibonacci(f1, f2, max_val):
    sequence = [1, 2]
    next_val = sequence[-1] + sequence[-2]
    while next_val < max_val:
        next_val = sequence[-1] + sequence[-2]
        sequence.append(next_val)
    return sequence
   
if __name__ == "__main__":
    if argc != 4:
        print(usage)
        sys.exit(1)
    try:
        for number in fibonacci(int(sys.argv[1]), int(sys.argv[2]),
                                int(sys.argv[3])):
            print(number)
    except ValueError:
        print(usage)
        print("All values must be numeric")
