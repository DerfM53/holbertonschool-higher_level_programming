#!/usr/bin/python3
"""This module defines the BaseGeometry class."""


class BaseGeometry:
    """A base class for geometry-related classes."""

    def area(self):
        """Return area of Rectangle"""
        return self._Rectangle__width * self._Rectangle__height

    def integer_validator(self, name, value):
        """
        Validate that a value is a positive integer.
        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than or equal to 0.
        """
        if not isinstance(value, int) or isinstance(value, bool):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """
    A class representing a rectangle,
    inheriting from BaseGeometry.
    """
    def __init__(self, width, height):
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        """return sence represantative of rectangle"""
        return ("[Rectangle] {}/{}".format(self.__width, self.__height))


class Square(Rectangle):
    """
    A class of Rectangle for Square classes
    who take an attribute size
    """
    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size
        self._Rectangle__width = size
        self._Rectangle__height = size

    def __str__(self):
        """return sence represantative of Square"""
        return ("[Square] {}/{}".format(self.__size, self.__size))
