#!/usr/bin/python3
"""Define Rectangle class"""


class Rectangle:
    """Representation of rectangle"""

    number_of_instances = 0
    print_symbol = "#"

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Return the biggest rectangle based on the area"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

    def __init__(self, width=0, height=0):
        """Initialise the rectangle"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def __del__(self):
        """Print a string when an instance has been deleted"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

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
        """Return the perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        """Return printed "#" character of the rectangle"""
        character = ""
        if self.__width != 0 and self.__height != 0:
            character += "\n".join(str(self.print_symbol) * self.__width
                                for j in range(self.__height))
        return character

    def __repr__(self):
        """returns a printed character representation of the rectangle for reproduction"""
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)
