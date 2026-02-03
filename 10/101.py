#!/usr/bin/python3
#==========
# 101.py
#==========

'''

indicator light diagrams
button wire schematics
joltage requirements for each machine

ONE MACHINE PER LINE
- 1 indicator light diagram []
- 1+ BUTTON wire schematics ()
IGNORE: - joltage requirements {}

INDICATOR LIGHTS
to start a machine, its indicator lights must match those whosn in the diagram
. = off
# = on
indicator lights are initially off
[.##.]  4 indicator lights. off, on, on, off

BUTTONS
you can toggle the state of idicator lights by pushing any of the listed buttons
each button lists which indicator lights it toggles
0=1st light, 1=2nd light, ...
you have to push each button an integer number of times
(0,3,4) - each time you press the button, you toggle light0, light3, light4

FIND FEWEST TOTAL PRESSES REQUIRED TO CORRECTLY CONFIGURE ALL THE INDICATOR LIGHTS FOR THE MACHINES IN YOUR LIST

[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
[...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}
[.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}
'''

import sys
import re
import collections


def bfs (start      # in: list of char - hence mutable
        ,expected   # in: list of char - hence mutable
        ,sb_list    # in: list of button lists (integers) [ [1,3], [2], [2,3], [0,2], [0,1], [3,5,4,7] ]
        ):

    # (item (char list), #steps)
    q = collections.deque()

    q.append((start,0))

    while q:
        qitem = q.popleft()

        s = qitem[0]

        num_steps = qitem[1]

        if s == expected:
            print ("found it. s=", s, " expected=", expected, " #steps=", num_steps)
            return num_steps

        # for each button list
        for lst in sb_list:

            t = s.copy()

            # for each switch we need to toggle
            for idx in lst:
                if t[idx] == ".":
                    t[idx] = "#"
                else:
                    t[idx] = "."

            q.append((t,num_steps+1))
    

# main

sum = 0

for line in sys.stdin:

    line = line.rstrip()    # remove any white space from end of string

    print ("line:", line)

    match = re.search(r'\[(.*)] (\(.*\))', line)

    if not match:
        print ("invalid line", line)
        sys.exit(-1)

    print ("expected:", match.group(1), " switches:", match.group(2))

    expected = list(match.group(1))

    print ("expected - list:", expected)


    switch_banks_str = match.group(2)

    # list of lists

    sb_pattern = r'\(([^)]+)\)'

    sb_list_str = re.findall(sb_pattern, switch_banks_str)

    # [ [1,3], [2], [2,3], [0,2], [0,1], [3,5,4,7] ]
    sb_list = []

    for sb in sb_list_str:
        l = sb.split(',')

        # [1,3]
        sb_list_item = []

        for ll in l:
            sb_list_item.append(int(ll))    

        sb_list.append(sb_list_item)

    print (sb_list)

    # at this point, we have expected [.##.] and a list of lists

    start = ["."] * len (expected)

    print ("start:", start)
    print ("")

    sum += bfs (start, expected, sb_list)

print ("sum=", sum)
