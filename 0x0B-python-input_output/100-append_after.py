#!/usr/bin/python3
""" append_after function documentation """


def append_after(filename="", search_string="", new_string=""):
    """ Append a new_string after search_string

    Args:
        filename: filename
        search_string: string to search
        new_string: string to append

    """


    with open(filename, 'r+', encoding="utf-8") as fl:
        for current_string in fl:
            if search_string in current_string:
                fl.write(new_string)
            else:
                continue
    fl.close()
    return fl
