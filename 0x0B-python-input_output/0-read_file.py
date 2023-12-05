#!/usr/bin/python3
"""Read file function documentation"""


def read_file(filename=""):
    """ Reads from a file"""

    with open(filename, encoding="utf-8") as fl:
        print(fl.read(), end='')
