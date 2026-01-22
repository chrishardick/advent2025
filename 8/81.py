#!/usr/bin/python3
#==========
# 81
#==========

'''
we have points in 3d space
for each point, we can find the distance to each other point 
ctrl = 20*20
in = 1000*1000 1MM - not too bad
'''

import sys
from collections import defaultdict

num_items = 10

if len(sys.argv) > 1:
    num_items = int(sys.argv[1])

print ("num_items=", num_items)


#
# main
#



# 1)    populate points list
#       [
#           (x1,y1,z1), 
#           (x2,y2,z2), 
#           ...
#       ]

points = []

start = None

for line in sys.stdin:

    line = line.rstrip()    # remove any white space from end of string

    flds = line.split(',')

    if len(flds) != 3:
        print ("invalid line:", line)
        sys.exit(-1)

    x = int(flds[0])
    y = int(flds[1])
    z = int(flds[2])

    points.append((x,y,z))


#==========
# 2) populate dist dictionary
#    [p1,p2] = length
#==========
dist = {}

for i in range (len(points)):
    for j in range (len(points)):

        if i == j:
            continue

        p1 = points[i]  # (x,y,z)
        p2 = points[j]  # (x,y,z)

        if (p2,p1) in dist:
            continue

        x_val = (points[j][0] - points[i][0]) ** 2
        y_val = (points[j][1] - points[i][1]) ** 2
        z_val = (points[j][2] - points[i][2]) ** 2

        d = (x_val + y_val + z_val) ** 0.5

        dist[(p1,p2)] = d


'''
traverse the 1st 10 lengths. 

we basically want: p1 => circuit1, p2 => circuit1

for the remaining shortest distances, check each one, 
'''


print ("unsorted distances")

for key in dist:
    print ("%s: %s" % (key,dist[key]))

print ("")

# 3) sort by distance 
# (x11,y11,z11),(x12,y12,z12) => length
# (x21,y21,z21),(x22,y22,z22) => length
# ...

sorted_dist = dict(sorted(dist.items(), key=lambda item: item[1]))

print ("SORTED distances")

for key in sorted_dist:
    print ("%s: %s" % (key,sorted_dist[key]))

print ("")


# go thru sorted dictionary
# 1st element - add 2 items to dict with rhs=0
# 2nd-nth element, if either of the points are already in dict, add these items also to dict with same rhs
# else (neither pair is in list), add them to dict rhs=2

# exit after making 10/1000 shortest connections - how many circuits will there be? - 11
# c1 = 5 junction boxes
# c2 = 4 junction boxes
# c3 = 2 junction boxes

# multiply sizes of largest 3 circuits

i = 0
circuit = 0

# circuit => set of points
circuit_to_pts = defaultdict(set)

# point => circuit
pt_to_circuit = {}

# (p1,p2): distance

for key in sorted_dist:

    p1 = key[0]            
    p2 = key[1]            

    if i == 0:
    
        print ("i=0: p1=", p1, "p2=", p2)

        pt_to_circuit[p1] = circuit
        pt_to_circuit[p2] = circuit

        circuit_to_pts[circuit].add(p1)
        circuit_to_pts[circuit].add(p2)

        print ("circuit=",circuit,"pts=",circuit_to_pts[circuit])

        circuit  += 1

    else:

        print ("p1=", p1, "p2=", p2)

        if p1 in pt_to_circuit and p2 in pt_to_circuit:

            # need to combine

            c1 = pt_to_circuit[p1]
            c2 = pt_to_circuit[p2]

            print ("found both. combine", c1, "and", c2)

            for pt in circuit_to_pts[c1]:
                circuit_to_pts[circuit].add(pt)
                pt_to_circuit[pt] = circuit

            for pt in circuit_to_pts[c2]:
                circuit_to_pts[circuit].add(pt)
                pt_to_circuit[pt] = circuit
            
            if c1 in circuit_to_pts:
                del circuit_to_pts[c1]

            if c2 in circuit_to_pts:
                del circuit_to_pts[c2]

            print ("cicruit", circuit, "pts=", circuit_to_pts[circuit])

            circuit += 1

        elif p1 in pt_to_circuit:

            circuit_num = pt_to_circuit[p1]

            pt_to_circuit[p2] = circuit_num

            circuit_to_pts[circuit_num].add(p2)

            print (p1, "found. adding", p2, "to", circuit_num, "pts=",circuit_to_pts[circuit_num])

        elif p2 in pt_to_circuit:

            circuit_num = pt_to_circuit[p2]

            pt_to_circuit[p1] = circuit_num

            circuit_to_pts[circuit_num].add(p1)

            print (p2, "found. adding", p1, "to", circuit_num, "pts=",circuit_to_pts[circuit_num])

        else:
           
            # neither are currently part of an existing circuit

            print ("neither are part - creating new circuit")

            pt_to_circuit[p1] = circuit
            pt_to_circuit[p2] = circuit

            circuit_to_pts[circuit].add(p1)
            circuit_to_pts[circuit].add(p2)

            print ("circuit", circuit, "pts=", circuit_to_pts[circuit])
            circuit += 1

    print ()

    i += 1   

    if i == num_items:
        print ("got to 10")
        break


print ("")


lengths_list = []

for key in circuit_to_pts:
    print ("circuit=", key, "len=", len(circuit_to_pts[key]), "pts:", circuit_to_pts[key])
    lengths_list.append(len(circuit_to_pts[key]))

lengths_list.sort(reverse=True)

product = 1

i = 0
for l in lengths_list:

    product *= l

    i += 1

    if i == 3:
        break

print ("PRODUCT=", product)
