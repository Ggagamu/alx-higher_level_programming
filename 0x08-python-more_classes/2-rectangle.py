#!/usr/bin/python3
"""Define Rectangle class"""


class Rectangle:
    """Representation of rectangle"""
    def __init__(self, width=0, height=0):
        """Initialise the rectangle"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get attribute, width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set attribute, width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get attribute, height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set attribute, height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return the area of the rectangle"""
        return (self.__width * self.__height)

    def perimeter(self):
        """returns the perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)
