#!/usr/bin/python3
#==========
# 92
#==========

'''
opposite tiles for a rectangle

rectangle must be entirely red or green

can only switch out files that are red or green
rectangle can only include red or green tiles

red tiles have not changed
every red tile is connected to the red tile before or after it by a straight line of green tiles
the list wraps. so the first red tile is also connected to the last red tile

'''

import sys

from collections import defaultdict


'''
p1 (x,y) is top left
p2 (x,y) is bottom right
'''
def valid_rect (p1, p2, min_max):
    
    rect_min_x = min(p1[0],p2[0])
    rect_max_x = max(p1[0],p2[0])

    rect_min_y = min(p1[1],p2[1])
    rect_max_y = max(p1[1],p2[1])

    for y in range (rect_min_y, rect_max_y+1):
        
        if y not in min_max:
            return False

        # if here, y is in min_max

        min_x = min_max[y][0]
        max_x = min_max[y][1]

        if rect_min_x < min_x:
            return False

        if rect_max_x > max_x:
            return False
       
    return True


# main

# 1)    populate points list
#       [
#           (x1,y1), 
#           (x2,y2), 
#           ...
#       ]
#
# 2)    populate
#       min_maxY[y] = (minX,maxX)
#       min_maxX[x] = (minY,maxY)
        
        

points = []

min_max = {}

minX = None
maxX = None

minY = None
maxY = None

# [x] = (min, max)
minMaxX = {}

for line in sys.stdin:

    line = line.rstrip()    # remove any white space from end of string

    flds = line.split(',')

    if len(flds) != 2:
        print ("invalid line:", line)
        sys.exit(-1)

    x = int(flds[0])
    y = int(flds[1])

    points.append((x,y))

    if minX == None or x < minX:
        minX = x

    if maxX == None or x > maxX:
        maxX = x

    if minY == None or y < minY:
        minY = y

    if maxY == None or y > maxY:
        maxY = y

    if x not in minMaxX:
        minMaxX[x] = (y,y)
    else:
        m0 = minMaxX[x][0]
        m1 = minMaxX[x][1]

        if y < m0:
            m0 = y

        if y > m1:
            m1 = y

        minMaxX[x] = (m0, m1)


print ("minMaxX...")

for x in minMaxX:
    print ("x=", x, " min_y=", minMaxX[x][0], " max_y=", minMaxX[x][1])


#
# points2[]
#

points2 = []

for x in minMaxX:
    if minMaxX[x][1]-minMaxX[x][0] > 1:
        for y in range(minMaxX[x][0]+1, minMaxX[x][1]):
            points2.append((x,y))


all_points = points + points2

# [y] = (minX, maxX)
minMaxY = {}

for pt in all_points:

    x = pt[0]
    y = pt[1]

    if y not in minMaxY:
        minMaxY[y] = (x, x)
    else:
        m0 = minMaxY[y][0]
        m1 = minMaxY[y][1]

        if x < m0:
            m0 = x

        if x > m1:
            m1 = x

        minMaxY[y] = (m0, m1)
    

#==========
# 2) populate areas dictionary
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

        if valid_rect(p1, p2, minMaxY):
            a = (abs(points[j][0]-points[i][0])+1) * (abs(points[j][1]-points[i][1])+1)
            areas[(p1,p2)] = a
            # print ("VALID RECt:", p1, p2, " area=", a)
        # else:
            # print ("not a valid rect:", p1, p2)



print ("unsorted areas")

for key in areas:
    print ("%s: %s" % (key,areas[key]))

print ("")

# 3) sort by area
# (x11,y11),(x12,y12) => length
# ...

sorted_areas = dict(sorted(areas.items(), key=lambda item: item[1]))

print ("SORTED areas")

for key in sorted_areas:
    print ("%s: %s" % (key,sorted_areas[key]))

