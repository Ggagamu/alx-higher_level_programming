#!/usr/bin/python3
""" The JSON function documentation"""


import json


def to_json_string(my_obj):
    """ Create the JSON representation of an object

    Args:
        my_obj: object to convert to JSON
        Return: JSON representation
        """
    return json.dumps(my_obj)
