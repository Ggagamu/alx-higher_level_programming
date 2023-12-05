#!/usr/bin/python3
"""BaseGeometry class and Rectangle subclass documentation"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """An inheritance of Rectangle class"""
    def __init__(self, size):
        """Get and set dimensions of the square"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """"Return the area of the square"""
        return self.__size ** 2
