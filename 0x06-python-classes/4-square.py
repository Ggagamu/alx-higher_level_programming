#!/usr/bin/python3
"""Defines a class Square"""


class Square:
    """Represent class square"""

    def __init__(self, size=0):
        """initialize the square
        Args:
            size (int): size of a side of the square
        Returns:
            None
        """
        self.size = size

    def area(self):
        """calculate the square's area
        Returns:
            The area of the square
        """
        return (self.__size) ** 2

    @property
    def size(self):
        """Gets __size
        Returns:
            The size of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Sets __size
        Args:
            value (int): the size of a size of the square
        Returns:
            None
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        else:
            if value < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = value
