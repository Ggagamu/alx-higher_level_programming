#!/usr/bin/python3
"""BaseGeometry class documentation"""


class BaseGeometry:
    """Class with public instance methods"""
    def area(self):
        """Raise an exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates that value is an integer"""
        if not isinstance(value, int):
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
