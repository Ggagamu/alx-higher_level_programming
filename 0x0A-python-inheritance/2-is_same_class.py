#!/usr/bin/python3
"""Documentation for is_same_class function"""


def is_same_class(obj, a_class):
    """Returns true if obj is the sub class of a_class, otherwise false"""
    return (type(obj) == a_class)
