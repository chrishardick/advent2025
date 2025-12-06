#!/usr/bin/python3
#==========
# 62
#==========

import sys

#
# main
#

matrix = []

for line in sys.stdin:

    print ("line=",line)

    chars = []

    for c in line:
        chars.append(c)

    print ("#char=",len(chars))

    matrix.append(chars)

    print ("")
    

total = 0
subtotal = 0

for x in range (len(matrix[0])):

    if matrix[len(matrix)-1][x] != ' ' and matrix[len(matrix)-1][x] != '\n':

        # found a new op

        print ("new op - subtotal=",subtotal)

        total += subtotal

        op = matrix[len(matrix)-1][x]

        print ("op=",op)

        if op == '*':
            subtotal = 1
        else:
            subtotal = 0

    num = 0

    for y in range (len(matrix)-1):

        if matrix[y][x] == ' ' or matrix[y][x] == '\n':
            continue

        if num == 0:
            num = int(matrix[y][x])
        else:
            num = num*10 + int(matrix[y][x])

    if num == 0:
        continue

    print ("num=",num)

    if op == '*':
        subtotal *= num
    else:
        subtotal += num

total += subtotal

print ("total=",total)
        
