#!/usr/bin/python3
"""Defines a Rectangle class"""


class Rectangle:
    """Representation of rectangle class"""
    def __init__(self, width=0, height=0):
        """Initialise the rectangle"""
        self.height = height
        self.width = width

    @property
    def width(self):
        """Get width of rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set width of rectangle"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get height attribute of rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set height attribute of rectangle"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
