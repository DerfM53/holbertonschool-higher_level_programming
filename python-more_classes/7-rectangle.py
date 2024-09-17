#!/usr/bin/python3
"""Module that define a rectangle class"""


class Rectangle:
    """A class that define a rectangle with instance count"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Initialize a new Rectangle instance
        and incremente de instance count
        """
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
            Rectangle.number_of_instances += 1

    def __del__(self):
        """
        Print a message when object is delete and
        decremented the instance count
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    def __str__(self):
        """
        Return rectangle reprentative with # symbol
        or other symbol or string user choice
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        rectangle = []
        for _ in range(self.__height):
            row = str(self.print_symbol) * self.__width
            rectangle.append(row)
        return "\n".join(rectangle)

    def __repr__(self):
        """Return representative str of rectangle"""
        return eval(f"'Rectangle({self.__width}, {self.__height})'")

    def area(self):
        """return area of rectangle"""
        return self.__height * self.__width

    def perimeter(self):
        """return perimeter of rectangle"""
        return (self.__height * 2) + (self.__width * 2)

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