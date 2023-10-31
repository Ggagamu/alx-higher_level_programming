#!/usr/bin/python3
for u in range(0, 10):
    for o in range(0, 10):
        if u >= o:
            continue
        elif u == 8 and o == 9:
            print("{}{}".format(u, o))
        else:
            print("{}{}, ".format(u, o), end='')
