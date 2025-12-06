#!/usr/bin/python3
#==========
# 52
#==========

import sys

#
# main
#

# list of lists
# [r1,r2]
fresh_ranges = []

for line in sys.stdin:

    line = line.rstrip()    # remove any white space from end of string

    if len(line) == 0:
        break

    rr = line.split("-")

    rr[0] = int(rr[0])
    rr[1] = int(rr[1])

    fresh_ranges.append(rr)

print ("#ranges=",len(fresh_ranges))


print ("sorting ranges...")

ranges_sorted = sorted(fresh_ranges, key=lambda x: x[0])

print ("done sorting ranges")


merged_list = []


print ("merging sorted ranges...")

# traverse sorted ranges and merge

for i in range(len(ranges_sorted)):
    
    elem = ranges_sorted[i]

    if i == 0:

        merged_list.append ((elem[0],elem[1]))

    else:

        curr_end = int(merged_list[len(merged_list)-1][1])

        if curr_end >= elem[0]:             # overlap
            if elem[1] > curr_end:
                merged_list[len(merged_list)-1][1] = elem[1]

        else:                               # no overlap
            merged_list.append(elem)
                

num_fresh = 0

for rng in merged_list:

    num_fresh += (rng[1] - rng[0] + 1)

print ("#fresh=",num_fresh)

