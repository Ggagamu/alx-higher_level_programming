#!/usr/bin/python3
for u in range(122, 96, -1):
    if u % 2 != 0:
        print("{:c}".format(u - 32), end='')
    else:
        print("{:c}".format(u), end='')
