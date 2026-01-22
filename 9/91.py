#!/usr/bin/python3
#==========
# 91
#==========

'''
tile floor with interesting pattern
some of the tiles are red
find the largest rectangle that uses red tiles for two of its opposte corners
puzzle input: where red tiles are located
'''

import sys

# main

# 1)    populate points list
#       [
#           (x1,y1), 
#           (x2,y2), 
#           ...
#       ]

points = []

start = None

for line in sys.stdin:

    line = line.rstrip()    # remove any white space from end of string

    flds = line.split(',')

    if len(flds) != 2:
        print ("invalid line:", line)
        sys.exit(-1)

    x = int(flds[0])
    y = int(flds[1])

    points.append((x,y))


#==========
# 2) populate dist dictionary
#    [p1,p2] = length
#==========
areas = {}

for i in range (len(points)):
    for j in range (len(points)):

        if i == j:
            continue

        p1 = points[i]  # (x,y,z)
        p2 = points[j]  # (x,y,z)

        if (p2,p1) in areas:
            continue

        a = (abs(points[j][0]-points[i][0])+1) * (abs(points[j][1]-points[i][1])+1)

        areas[(p1,p2)] = a


print ("unsorted areas")

for key in areas:
    print ("%s: %s" % (key,areas[key]))

print ("")

# 3) sort by distance 
# (x11,y11,z11),(x12,y12,z12) => length
# (x21,y21,z21),(x22,y22,z22) => length
# ...

sorted_areas = dict(sorted(areas.items(), key=lambda item: item[1]))

print ("SORTED areas")

for key in sorted_areas:
    print ("%s: %s" % (key,sorted_areas[key]))

