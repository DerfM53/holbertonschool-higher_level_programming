#!/usr/bin/python3
"""
This module implements an abstract Shape class and its concrete subclasses.

It demonstrates the use of abstract base classes and duck typing in Python.
The module includes:
- An abstract Shape class
- Concrete Circle and Rectangle classes
- A shape_info function that uses duck typing to print shape information
"""

from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """Abstract class representing a shape"""

    @abstractmethod
    def area(self):
        """Calculate the area of the shape"""
        pass

    @abstractmethod
    def perimeter(self):
        """Calculate the perimeter of the shape"""
        pass


class Circle(Shape):
    """Subclass of shape defining a circle"""

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        """Return the area of the circle"""
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        """Return the perimeter of the circle"""
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """Subclass of chape defining a rectangle"""

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        """Return the area of rectangle"""
        return self.width * self.height

    def perimeter(self):
        """Return the perimeter of rectangle"""
        return 2 * (self.width + self.height)


def shape_info(shape):
    """
    Print the area and perimeter of a geometric shape.

    This function uses duck typing to call the area() and perimeter()
    methods on the shape object passed as an argument,
    without checking its specific type.

    Args:
        shape: An object representing a geometric shape.
               Must have area() and perimeter() methods.

    Prints:
        Displays the area and perimeter of the shape on separate lines.

    Raises:
        AttributeError: If the shape object doesn't have
        area() or perimeter() methods.
    """
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")
