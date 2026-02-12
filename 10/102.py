#!/usr/bin/python3
#==========
# 102.py
#==========

'''

indicator light diagrams
button wire schematics
joltage requirements for each machine

ONE MACHINE PER LINE
====================

[ indicator lights .##. ]          () () () ()         { joltage requirements }


IGNORE - 1 indicator light diagram []
- 1+ BUTTON wire schematics ()
- joltage requirements {}

BUTTONS
each button now indicates which counters it affects
0 = 1st counter, 1 = 2nd counter, ...
each time you push a button, each listed counter is increased by 1
(1,3) each time you push the button, the 2nd and 4th counters would be increased by 1

you have to push each button an integer number of times

JOLTAGE (TARGET)
{3,5,4,7} 
    - machine has 4 counters which are initially 0 
    - the goal is to simultaneously configure the first counter to be 3, 
        the 2nd counter to 5, the 3rd counter to 4, and the 4th to be 7
COUNTERS
[0,1,2,3] w/ button (1,3) => [0,1+1,2,3+1] = [0,2,2,4]

FIND FEWEST TOTAL PRESSES REQUIRED TO CORRECTLY CONFIGURE EACH MACHINE'S JOLTAGE LEVEL COUNTERS 

[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7} 
[...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}
[.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}
'''

import sys
import re
import collections


def bfs (start      # in: int list - hence mutable [0,0,0,0]
        ,expected   # in: int list - hence mutable - joltage [3,5,4,7]
        ,sb_list    # in: list of button lists (integers) [ [1,3], [2], [2,3], [0,2], [0,1], [3,5,4,7] ]
        ):

    print ("bfs: start=", start, " expected=", expected, " sb_list=", sb_list)

    verbose = False

    # (item (char list), #steps)
    q = collections.deque()

    q.append((start,0))

    while q:

        
        qitem = q.popleft()

        verbose and print ("qitem=",qitem)

        s = qitem[0]

        num_steps = qitem[1]

        potential_match = True
        match = True

        for i in range(len(s)):
            if s[i] < expected[i]:
                match = False
                break   # not equal
            elif s[i] > expected[i]:
                potential_match = False
                match = False
                break
            if s[i] == expected[i]:
                continue

        if match:
            print ("found it. s=", s, " expected=", expected, " #steps=", num_steps)
            return num_steps

        elif not potential_match: # already went too many steps
            if verbose:
                print ("not a potential match. s=", s, " expected=", expected, " #steps=", num_steps)

                for i in range(len(s)):
                    print ("i=", i, " s[i]=", s[i], " exp[i]=", expected[i])

            continue

        else:
            if verbose:
                print ("potential match. s=", s, " expected=", expected, " #steps=", num_steps)
            
                for i in range(len(s)):
                    print ("i=", i, " s[i]=", s[i], " exp[i]=", expected[i])

            
        # for each button list
        for lst in sb_list:

            verbose and print ("    lst=",lst)

            t = s.copy()

            # for each switch we need to increment
            for idx in lst:
                t[idx-1] += 1

            verbose and print ("    t=",t, " num_steps=", num_steps+1, " exp=", expected)
            q.append((t,num_steps+1))
    

# main

sum = 0

for line in sys.stdin:

    line = line.rstrip()    # remove any white space from end of string

    print ("line:", line)

    match = re.search(r'\[(.*)] (\(.*\)) \{(.*)\}', line)

    if not match:
        print ("invalid line", line)
        sys.exit(-1)


    print ("expected:", match.group(1), " switches:", match.group(2), " joltage:", match.group(3))

    # IGNORE 1ST FIELD
    ignore_lst = list(match.group(1))


    # SWITCH BANKS

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


    # JOLTAGE

    joltage_str = match.group(3)

    print ("joltage_str=", joltage_str)

    joltage_lst = []

    for j in joltage_str.split(','):
        joltage_lst.append(int(j))

    print ("joltage_lst=", joltage_lst)


    # at this point, we have expected [.##.] and a list of lists

    start = [0] * len (joltage_lst)

    print ("start:", start)
    print ("")

    sum += bfs (start, joltage_lst, sb_list)

print ("sum=", sum)
