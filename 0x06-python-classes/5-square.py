#!/usr/bin/python3
"""Defines a square class"""


class Square:
    """Represent a square class"""

    def __init__(self, size=0):
        """Initialize square class
        Args:
            size (int): size of a side of the square
        Returns:
            None
        """
        self.size = size

    def area(self):
        """Calculate square's area
        Returns:
            The square's area
        """
        return (self.__size) ** 2

    @property
    def size(self):
        """Get __size
        Returns:
            The size square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Set __size
        Args:
            value (int): size of a side of the square
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

    def my_print(self):
        """Print the square
        Returns:
            None
        """
        if self.__size == 0:
            print()
            return
        for i in range(self.__size):
            print("#" * self.__size)
