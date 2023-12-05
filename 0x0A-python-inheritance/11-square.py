#!/usr/bin/python3
"""BaseGeometry class and subclass Rectangle documentation"""


class BaseGeometry:
    """Class with public instance methods"""
    def area(self):
        """Raise an exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate that value is an integer"""
        if not isinstance(value, int):
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """An inheritance of a BaseGeometry class"""
    def __init__(self, width, height):
        """Get and set the dimensions of the rectangle"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """Return the area of the rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """Special representation of the rectangle as a string"""
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)


class Square(Rectangle):
    """An inheritance of Rectangle class """
    def __init__(self, size):
        """Get and set the dimensions of the square"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """"Return the area of the square"""
        return self.__size ** 2

    def __str__(self):
        """Special reepresentation of the square as a string"""
        return "[Square] {:d}/{:d}".format(self.__size, self.__size)
