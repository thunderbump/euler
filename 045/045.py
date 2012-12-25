#!/usr/bin/python

import sys

argc = len(sys.argv)
usage = """045.py
Computes the first two triangle numbers that are also pentagonal and hexagonal.
"""

def triangle(max_num, start=[1]):
    idx = len(start)
    nxt = start[-1]
    while nxt < max_num:
        idx += 1
        nxt = (idx * (idx + 1)) / 2
        start.append(nxt)
    return start

def pentagonal(max_num, start=[1]):
    idx = len(start)
    nxt = start[-1]
    while nxt < max_num:
        idx += 1
        nxt = (idx * ((3 * idx) - 1)) / 2
        start.append(nxt)
    return start

def hexagonal(max_num, start=[1]):
    idx = len(start)
    nxt = start[-1]
    while nxt < max_num:
        idx += 1
        nxt = idx * ((2 * idx) - 1)
        start.append(nxt)
    return start

if __name__ == "__main__":
    if argc > 2:
        print(usage)
        sys.exit(1)

    index = 0
    allthethings = []
    starting_size = 1000
    testrange = 1000
    tri = triangle(starting_size)
    pen = testpen = pentagonal(starting_size)
    hexa = testhexa = hexagonal(starting_size)

    while len(allthethings) < 3:
        if len(tri) == index:
            starting_size = starting_size * 2
            tri = triangle(starting_size)
            pen = pentagonal(starting_size)
            hexa = hexagonal(starting_size)
            testpen = pen[-index:]
            testhexa = hexa[-index:]
            
        if tri[index] in testpen and tri[index] in testhexa:
            allthethings.append(tri[index])
        if index % 100 == 0:
            print index, allthethings, len(tri), len(pen), len(hexa)
        index += 1
    print allthethings
    #print triangle(100)
    #print pentagonal(100)
    #print hexagonal(100)
