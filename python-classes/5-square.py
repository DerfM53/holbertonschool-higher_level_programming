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
        """Return area of square"""
        return self.__size * self.__size

    def my_print(self):
        """print a square with symbol #"""
        if self.__size == 0:
            print()
        else:
            for a in range(self.__size):
                for b in range(self.__size):
                    print("#", end="")
                print()

    @property
    def size(self):
        """User can get the value size"""
        value = self.__size
        return value

    @size.setter
    def size(self, value):
        """
        User can change the value size
        if this value is an integer and >= 0
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
