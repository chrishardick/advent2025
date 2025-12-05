#!/usr/bin/python3
#==========
# 42
#==========

import sys

def is_valid (x, y, mtx):

    if x < 0 or x >= len(mtx[0]):
        return False

    if y < 0 or y >= len(mtx):
        return False

    return True


# given x,y and mtx, return True if can access (has < 4 adjacent rolls)
def can_access(x, y, mtx):

    if mtx[y][x] != '@':
        return False


    l = []
    l.append((x,y-1))   # up
    l.append((x,y+1))   # down
    l.append((x-1,y))   # left
    l.append((x+1,y))   # right
    l.append((x-1,y-1)) # diag top left
    l.append((x+1,y-1)) # diag top right
    l.append((x-1,y+1)) # diag bot left
    l.append((x+1,y+1)) # diag bot right

    num_adj = 0

    for pt in l:
        xx = pt[0]
        yy = pt[1]

        if not is_valid(xx,yy,mtx):
            continue

        if mtx[yy][xx] == '@':
            num_adj += 1

            if num_adj > 3:
                return False

    return True

            
        

#
# main
#

matrix = []


for line in sys.stdin:

    line = line.rstrip()    # remove any white space from end of string

    print ("line=",line)

    l = []

    for c in line:
        l.append(c)

    matrix.append(l)


num_rm = 0


while True:

    to_rm = []

    for y in range (len(matrix)):
        for x in range (len(matrix[0])):
            if can_access(x,y,matrix):
                to_rm.append((x,y))
                num_rm += 1

    for pt in to_rm:
        x = pt[0]
        y = pt[1]

        matrix[y][x] = '.'

    if len(to_rm) == 0:
        break

print ("num_rm=",num_rm)
