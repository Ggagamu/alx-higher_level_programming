#!/usr/bin/python3
""" Module that creates an Object from a JSON file
"""
import json


def load_from_json_file(filename):
    """ Create an Object from a JSON file

    Args:
        filename: file name
    """
    with open(filename, 'r', encoding="utf-8") as fl:
        return json.load(fl)
