#!/usr/bin/python3
""" from_json_string module documentation"""


import json


def from_json_string(my_str):
    """ Return an object by a JSON representation

    Args:
        my_str: JSON string
    """
    return json.loads(my_str)
