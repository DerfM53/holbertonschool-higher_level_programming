#!/usr/bin/python3
"""
This is a module that provides a function to add two integers.

The main function in this module is add_integer, which takes two
numbers (integers or floats) and returns their sum as an integer.
"""


def add_integer(a, b=98):
    """
    Adds two integers.

    Parameters:
    a (int or float): The first number.
    b (int or float, optional): The second number. Defaults to 98.

    Returns:
    int: The sum of a and b.

    Raises:
    TypeError: If a or b is not an integer or a float.
    OverflowError: If a or b is a float that's too
    large to convert to an integer.

    Examples:
    >>> add_integer(1, 2)
    3
    >>> add_integer(100, -2)
    98
    >>> add_integer(2)
    100
    >>> add_integer(100.3, -2)
    98
    >>> add_integer(4, "School")
    Traceback (most recent call last):
        ...
    TypeError: b must be an integer
    >>> add_integer(None)
    Traceback (most recent call last):
        ...
    TypeError: a must be an integer
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    try:
        return int(a) + int(b)
    except OverflowError:
        raise OverflowError("cannot convert float infinity to integer")
