#!/usr/bin/python3
def uppercase(str):
    for h in str:
        h = ord(h)
        if h >= 97 and h <= 122:
            h -= 32
        h = chr(h)
        print("{}".format(h), end='')
    print("")
