#!/usr/bin/python3
"""Module that defines a Square class"""


class Square:
    """A class that defines a square."""

    def __init__(self, size=0):
        """
        Initialize with an integer for value and check
        if value is an integer an value > 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """ return area of square"""
        return self.__size * self.__size
