#!/usr/bin/python3
#==========
# 31
#==========

import sys

sum = 0

for line in sys.stdin:

    line = line.rstrip()    # remove any white space from end of string

    print ("line=",line)

    # get 1st digit

    max_d1  = None
    idx_d1  = None

    for i in range(len(line)-1):

        d1 = int(line[i])

        if max_d1 == None or d1 > max_d1:
            max_d1 = d1
            idx_d1 = i


    max_d2 = None
    idx_d2 = None

    for i in range(idx_d1+1, len(line)):
    
        d2 = int(line[i])

        if max_d2 == None or d2 > max_d2:
            max_d2 = d2
            idx_d2 = i

    val = max_d1 * 10 + max_d2

    print ("val=",val)

    sum += val

print ("sum=",sum)
