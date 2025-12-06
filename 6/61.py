#!/usr/bin/python3
#==========
# 61
#==========

import sys

#
# main
#

matrix = []

for line in sys.stdin:

    line = line.rstrip()    # remove any white space from end of string

    flds = line.split(" ")

    flds_cln = []

    for f in flds:
        if len(f) != 0:
            flds_cln.append(f)

    print ("flds_cln=",flds_cln)

    matrix.append (flds_cln)

total = 0

for x in range (len(matrix[0])):

    op = matrix[len(matrix)-1][x]

    res = 0

    if op == '*':
        res = 1

    for y in range (len(matrix)-1):

        if op == '*':
            res *= int(matrix[y][x])
        else:
            res += int(matrix[y][x])

    total += res

print ("total=",total)
        
