#!/usr/bin/python3
"""Module that define a rectangle class"""


class Rectangle:
    """A class that define a rectangle"""

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle instance"""
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = width
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        elif height < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = height

    @property
    def width(self):
        """User can get the width value"""
        value = self.__width
        return value

    @width.setter
    def width(self, value):
        """
        User can change the value of width
        if the value is an integer and >= 0
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """User can get the height value"""
        value = self.__height
        return value

    @height.setter
    def height(self, value):
        """
        User can change the value of height
        if the value is an integer and >= 0
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
