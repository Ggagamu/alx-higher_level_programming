#!/usr/bin/python3
"""Define class square"""


class Square:
    """Represent a square"""

    def __init__(self, size=0):
        """initialize the square
        Args:
            size (int): size of side of square
        Returns:
            None
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        else:
            if size < 0:
                raise ValueError("size must be >= 0")
            self.__size = size
