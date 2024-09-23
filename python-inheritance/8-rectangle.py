#!/usr/bin/python3
"""This module defines the BaseGeometry class."""


class BaseGeometry:
    """A base class for geometry-related classes."""

    def area(self):
        """
        Calculate the area of the geometry.

        Raises:
            Exception: Always raises an exception with the message
                       "area() is not implemented".
        """
        raise Exception("area() is not implemented")

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
