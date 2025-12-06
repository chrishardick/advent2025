#!/usr/bin/python3
#==========
# 51
#==========

import sys

#
# main
#

ranges = []

for line in sys.stdin:

    line = line.rstrip()    # remove any white space from end of string

    if len(line) == 0:
        break

    rr = line.split("-")
  
    rr[0] = int(rr[0])
    rr[1] = int(rr[1])

    ranges.append(rr)

print ("#ranges=",len(ranges))

num_fresh = 0

for line in sys.stdin:

    ing = int(line.rstrip())

    for r in ranges:
        if ing >= r[0] and ing <= r[1]:
            num_fresh += 1
            break

print ("num_fresh=",num_fresh)


