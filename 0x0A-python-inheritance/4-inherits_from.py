#!/usr/bin/python3
"""inherits_from function documentation"""


def inherits_from(obj, a_class):
    """True if obj is a subclass of a_class, otherwise false"""
    return(issubclass(type(obj), a_class) and type(obj) != a_class)
