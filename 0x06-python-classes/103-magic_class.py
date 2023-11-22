#!/usr/bin/python3
"""Defines a class MagicClass that matches the same bytecode provided"""
import math


class MagicClass:
    """Represent a circle"""
    def __init__(self, radius=0):
        """Initialize the Magic Class"""
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """Calculate the area of the circle"""
        return (self.__radius ** 2) * math.pi

    def circumference(self):
        """Calculate the circumference of the circle"""
        return 2 * math.pi * self.__radius
