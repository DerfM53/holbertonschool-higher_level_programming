#!/usr/bin/python3
"""Module that defines a Square class"""


class Square:
    """A class that defines a square."""

    def __init__(self, size=0, position=(0, 0)):
        """
        Initialize with an integer for value and
        position and check if value is an integer an value > 0
        and position if is tuple with 2 integer.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
            self.__position = position

    def area(self):
        """
        Return area of square
        """
        return self.__size ** 2

    def my_print(self):
        """
        print a square with symbol #
        with value size and position
        """
        if self.__size == 0:
            print()
            return

        [print() for _ in range(self.__position[1])]
        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)

    @property
    def size(self):
        """User can get the value size"""
        value = self.__size
        return value

    @property
    def position(self):
        """User can get à position value"""
        value = self.__position
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

    @position.setter
    def position(self, value):
        """
        User can change the value position
        if this value is a tuple with 2 positives integer.
        """
        if not isinstance(value, tuple) or len(value) != 2 or \
           not all(isinstance(n, int) and n >= 0 for n in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value
