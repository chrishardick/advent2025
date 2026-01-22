#!/usr/bin/python3
#==========
# 82
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

print ("points")
for p in points:
    print (p)

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


i = 0
circuit = 0

# circuit => set of points
circuit_to_pts = defaultdict(set)

# point => circuit
pt_to_circuit = {}

# (p1,p2): distance


add_lst = []

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

        print ("append:", p1[0])
        add_lst.append(p1[0])

        print ("append:", p2[0])
        add_lst.append(p2[0])

        if p1 in pt_to_circuit and p2 in pt_to_circuit:

            # need to combine

            print ("found both. combine", p1, p2)

            c1 = pt_to_circuit[p1]
            c2 = pt_to_circuit[p2]

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

            print ("len(circuit_to_pts):",len(circuit_to_pts))

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

    one_circuit = False

    if len(circuit_to_pts) == 1:

        for c in circuit_to_pts:
            if len(circuit_to_pts[c]) == len(points):
                print ("got to 1 circuit. #items=",len(circuit_to_pts[c]))
                one_circuit = True
                break
            else:
                print ("# items=",len(circuit_to_pts[c]),"\n\n")

        if one_circuit:
            break
print ("")
print ("add_lst=", add_lst)

print ("RESULT: ", add_lst[len(add_lst)-1], add_lst[len(add_lst)-2], add_lst[len(add_lst)-1]*add_lst[len(add_lst)-2])
