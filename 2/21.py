#!/usr/bin/python3
#==========
# 21
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

        start   = int(start_str)
        end     = int(end_str)

        print ("start=", str(start), " end=", str(end), " size=", str(end-start))

        for x in range(start, end+1):

            str_x = str(x)

            len_str = len(str_x)

            # print ("str=",str_x, " len=",len_str)

            if (len_str % 2) == 0:
                # even length

                middle = int(len_str/2)

                lhs = str_x[:middle]
                rhs = str_x[middle:]

                # print ("lhs=",lhs, "rhs=",rhs)

                if lhs == rhs:
                    print ("found one:", str_x)

                    sum += int(str_x)


print ("sum=",sum)
