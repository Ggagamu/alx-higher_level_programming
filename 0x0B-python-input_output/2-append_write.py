#!/usr/bin/python3
""" append to a text file module documentation """


def append_write(filename="", text=""):
    """ Append to a text file

    Args:
        filename: filename
        text: string
    """

    with open(filename, 'a', encoding="utf-8") as fl:
        return fl.write(text)
