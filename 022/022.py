#!/usr/bin/python
"""Computes the sum of all "name scores" of words in a file. Name score are the
sum of one more than alphabetical offsets of all letters from A in the word"""

import sys

argc = len(sys.argv)
usage = """022.py data_file
Computes the sum of all "name scores" of words in a data_file. Name score are
the sum of one more than alphabetical offsets of all letters from A in the
word"""

def word_score(word, index):
    offset = ord('A') - 1
    score = 0
    for char in word:
         score += ord(char) - offset
    if word == "COLIN":
        print word, index, score * index
    return score * index

if argc != 2:
    print(usage)
    sys.exit(1)
try:
    total_score = 0
    data_file = open(sys.argv[1])
    data = data_file.readline()
    if data[-1] == '\n':
        data = data[:-1]
    if data[-1] == '\r':
        data = data[:-1]
    data = data.split('''","''')
    #missed a " at the beginning and end
    data[0] = data[0][1:]
    data[-1] = data[-1][:-1]
    data = sorted(data)
    for index, name in enumerate(data):
        total_score += word_score(name, index + 1)
    print(total_score)
except IOError, error:
    print(usage)
    print(error)
    sys.exit(1)
