#!/usr/bin/python

import sys

usage = """040.py d1 [d2 [d3 [...]]]
Finds the multiple of the numbers found at decimal places d1, d2, d3, etc in
the irrational number found by concatinating the positive integers after "0.",
eg 0.1234567891011..."""
argc = len(sys.argv)

def find_dec_vals(dec_list):
    #0 skipped in the first run through so this is hard coded
    below_10 = [x for x in dec_list if x < 10]
    
    len_digit_run = 9
    digit_size = 1
    next_pwr_10 = 10
    digit_vals = []
    while len(dec_list) != 0:
        if dec_list[0] >= next_pwr_10:
            print len_digit_run
            print dec_list, "--"
            dec_list = [dec - len_digit_run for dec in dec_list]
            print dec_list
            digit_size += 1
            len_digit_run = digit_size * next_pwr_10
            next_pwr_10 *= 10
            continue
        cur_digit = dec_list.pop(0)
        number_digits_in = cur_digit / digit_size + next_pwr_10 / 10
        print "-", number_digits_in, cur_digit, digit_size, cur_digit % digit_size
        digit_vals.append(int(str(number_digits_in)[cur_digit % digit_size]))
        print "#", digit_vals
    return digit_vals 

if __name__ == "__main__":
    if argc < 2:
        print(usage)
        sys.exit(1)
    try:
        decimals = [int(d) for d in sys.argv[1:]]
    except ValueError:
        print("all decimal places must be numeric")
        sys.exit(1)

    print decimals
    digit_values = find_dec_vals(sorted(decimals))
    print digit_values
    product = 1
    for value in digit_values:
        product *= value
    print product

