#!/usr/bin/python3
for u in range(0, 100):
    if u == 99:
        print("99")
    else:
        print("{0:0=2d}, ".format(u), end='')
