#!/usr/bin/python3
"""
This module implements an abstract Shape class and its concrete subclasses.

It demonstrates the use of abstract base classes and duck typing in Python.
The module includes:
- An abstract Shape class
- Concrete Circle and Rectangle classes
- A shape_info function that uses duck typing to print shape information
"""


import math
from abc import ABC, abstractmethod


class Shape(ABC):
    """Abstract class represently a shape"""

    @abstractmethod
    def area(self):
        """Method calculate the area of the shape"""
        pass

    @abstractmethod
    def perimeter(self):
        """Method calculate the perimeter of the shape"""
        pass


class Circle(Shape):
    """subclasse of shape defind a circle"""
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        """Return the area of the circle"""
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        """Return the perimeter of the circle"""
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """subclasse of chape defind a rectangle"""
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
    Affiche l'aire et le périmètre d'une forme géométrique.

    Cette fonction utilise le typage duck pour appeler les méthodes
    area() et perimeter() sur l'objet shape passé en argument,
    sans vérifier son type spécifique.

    Args:
        shape: Un objet représentant une forme géométrique.
        Doit avoir les méthodes area() et perimeter().

    Prints:
        Affiche l'aire et le périmètre de la forme sur des lignes séparées.

    Raises:
        AttributeError: Si l'objet shape n'a pas de méthode
        area() ou perimeter().
    """
    area = shape.area()
    perimeter = shape.perimeter()
    print("Area: {}".format(area))
    print("Perimeter: {}".format(perimeter))
