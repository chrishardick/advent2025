#!/usr/bin/python3
#==========
# 12
#==========

import sys

combo = 0

pos = 50

for line in sys.stdin:

    prev = pos

    line = line.rstrip()    # remove any white space from end of string

    left_right = line[0]

    num = int(line[1:])

    for i in range (num):

        if left_right == 'L':
            pos = (pos-1+100)%100

        elif left_right == 'R':
            pos = (pos+1)%100

        if pos == 0:
            combo += 1

print ("combo:", combo)
