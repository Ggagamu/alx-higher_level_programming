#!/usr/bin/python3
"""Define a class Square"""


class Square:
    """Represent a square

    Attributes:
        __size (int): size of a side of the square
    """
    def __init__(self, size=0):
        """initialize the square

        Args:
            size (int): size of a side of the square

        Returns:
            None
        """
        self.size = size

    def area(self):
        """Calculate the square's area"""
        return (self.__size) ** 2

    @property
    def size(self):
        """Get/set __size of square"""
        return self.__size

    @size.setter
    def size(self, value):
        """setter of __size"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        else:
            if value < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = value

    def __lt__(self, other):
        """Compare if square is less than another by area"""
        return self.size < other.size

    def __le__(self, other):
        """Compare if square is less than or equal to another by area"""
        return self.size <= other.size

    def __eq__(self, other):
        """Compare if square is equal to another by area"""
        return self.size == other.size

    def __ne__(self, other):
        """Compare if square is not equal to another by area"""
        return self.size != other.size

    def __ge__(self, other):
        """Compare if square is greater than or equal to another by area"""
        return self.size >= other.size

    def __gt__(self, other):
        """Compare if square is greater than another by area"""
        return self.size > other.size
