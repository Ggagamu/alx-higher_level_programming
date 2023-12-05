#!/usr/bin/python3
""" write file documentation """


def write_file(filename="", text=""):
    """ Function that writes to a text file

    Args:
        filename: filename
        text: string
    """

    with open(filename, 'w', encoding="utf-8") as fl:
        return fl.write(text)
