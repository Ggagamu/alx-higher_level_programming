#!/usr/bin/python3
""" add_attribute function documentation"""


def add_attribute(object, name, value):
    """ Add an attribute, else raise error """
    if not hasattr(object, "__dict__"):
        raise TypeError("can't add new attribute")
    if (not hasattr(object, name)):
        object.__setattr__(name, value)
