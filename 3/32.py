#!/usr/bin/python3
#==========
# 32
#==========

import sys

sum = 0

for line in sys.stdin:

    line = line.rstrip()    # remove any white space from end of string

    print ("line=",line)

    # val => idx list

    d = {}

    for i in range(len(line)):

        val = int(line[i])

        if val in d:
            d[val].append(i)
        else:
            d[val] = [i]


    bat = ""

    prev_idx = -1

    line_len = len(line)


    while len(bat) < 12:

        foundOne = False

        for k in sorted(d.keys(),reverse=True):

            for idx in d[k]:

                if idx > prev_idx and line_len - idx >= 12-len(bat):

                    # print ("foundOne", k)

                    foundOne = True
                    prev_idx = idx
                    bat += str(k)
                    break

            if foundOne:

                break

    bat_int = int(bat)
    print ("bat=",bat)
    print ("bat-int",bat_int)

    sum += bat_int

print ("sum=",sum)
