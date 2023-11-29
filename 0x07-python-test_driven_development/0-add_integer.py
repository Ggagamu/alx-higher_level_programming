#!/usr/bin/python3
"""
The "0-add_integer" module that adds two integers.
"""


def add_integer(a, b):
    """Return the sum of two numbers."""
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)
    return a + b
