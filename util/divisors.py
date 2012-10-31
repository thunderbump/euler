#!/usr/bin/python

import list_primes

def prime_divisors(number):
    primes = list_primes.get_primes_below(number)
    prime_divisor = {}
    for prime in primes:
        while number % prime == 0:
            if prime in prime_divisor:
                prime_divisor[prime] += 1
            else:
                prime_divisor[prime] = 1
            number /= prime
    if number != 1:
        prime_divisor[number] = 1
    return prime_divisor

def all_divisors(number):
    prime_divisor = prime_divisors(number)
    all_divisor = [1]
    for prime in prime_divisor.keys():
        appended_list = []
        for divisor in all_divisor:
            for mult in range(1, prime_divisor[prime] + 1):
                appended_list.append((prime ** mult) * divisor)
        for divisor in appended_list:
            all_divisor.append(divisor)
    return sorted(all_divisor)

