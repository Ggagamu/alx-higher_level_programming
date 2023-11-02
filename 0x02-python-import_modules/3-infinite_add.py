#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    arguments = len(argv)
    sum_args = 0
    for i in range(1, arguments):
        sum_args += int(argv[i])
    print(sum_args)
