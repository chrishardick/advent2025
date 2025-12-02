#!/usr/bin/python3
#==========
# 11
#==========

import sys

combo = 0

pos = 50

for line in sys.stdin:

    line = line.rstrip()    # remove any white space from end of string

    left_right = line[0]

    num = int(line[1:])

    if left_right == 'L':
        pos -= num
    elif left_right == 'R':
        pos += num

    while pos < 0:
        pos = 100+pos

    pos %= 100

    if pos == 0:
        combo += 1

    print ("line:", line)
    print ("left_right:", left_right)
    print ("num:", str(num))
    print ("pos:", str(pos))
    print ("")

print ("combo:", combo)
