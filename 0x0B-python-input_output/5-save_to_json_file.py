#!/usr/bin/python3
"""save_to_json module documentation"""


import json


def save_to_json_file(my_obj, filename):
    """ Write an object to a text file

    Args:
        my_obj: object
        filename: file name
    """
    with open(filename, 'w', encoding="utf-8") as fl:
        json.dumps(my_obj, fl)
