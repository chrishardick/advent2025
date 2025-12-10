#!/usr/bin/python3
#==========
# 72
#==========

import sys


# main

matrix = []

start = None

x=0
y=0

for line in sys.stdin:

    line = line.rstrip()    # remove any white space from end of string

    ll = []

    for c in line:
        ll.append(c)
        if c == "S":
            start = (x,y)

        x += 1

    matrix.append (ll)

    y += 1

if start == None:
    print ("start not found")
    sys.exit(1)


print ("line len=",len(matrix[0]))
print ("#lines=",len(matrix))


counts = [0] * len(matrix[0])

print ("counts=",counts)


for y in range (1,len(matrix)):

    for x in range (0,len(matrix[0])):

        if matrix[y-1][x] == 'S' or matrix[y-1][x] == '|':

            if matrix[y][x] == '^':

                sav = max(1,counts[x])
                counts[x] = 0

                if x-1 >= 0:
                    matrix[y][x-1] = '|'
                    counts[x-1] += sav
                if x+1 <= len(matrix[0])-1:
                    matrix[y][x+1] = '|'
                    counts[x+1] += sav

            elif matrix[y][x] == '.':

                matrix[y][x] = '|'

    print ("counts=",counts)

tot = 0
for i in counts:
    tot += i

print ("counts=",counts)

print ("total=",tot)
    
    
    

