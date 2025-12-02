#!/usr/bin/python3
#==========
# 22
#==========

import sys

sum = 0

for line in sys.stdin:

    line = line.rstrip()    # remove any white space from end of string

    rng_list = line.split(",")

    for rng in rng_list:

        start_end = rng.split("-")
        start_str   = start_end[0].lstrip('0')
        end_str     = start_end[1].lstrip('0')

        start   = int(start_str)        # range start
        end     = int(end_str)          # range end

        print ("start=", str(start), " end=", str(end), " size=", str(end-start))

        for x in range(start, end+1):

            str_x = str(x)

            len_str = len(str_x)

            '''
            12341234        1234    x2
            123123123       123     x3
            1212121212      12      x5
            1111111         1       x7

            9%8
            9%7
            9%6
            9%5
            9%4
            9%3=0
            9%2
            9%1=0
            '''

            for y in range(1,len_str+1):

                if (len_str % y) == 0:
                
                    # possible sub-division

                    substr_list = []

                    for z in range(0,len_str,y):    # 0, 3, 6

                        substr_list.append(str_x[int(z):int(z+y)])

                    match = False

                    for i in range (1,len(substr_list)):

                        match = True

                        if substr_list[i] != substr_list[0]:
                            match = False
                            break

                    if match:
                        print ("found one:", str_x)
                        sum += int(str_x)
                        break
                        

print ("sum=",sum)
