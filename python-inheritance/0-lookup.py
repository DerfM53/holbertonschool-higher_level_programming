#!/usr/bin/python3
"""
This module provides a function to lookup attribute
and methods of an object.
"""


def lookup(obj):
    """
    Returns a list of available attributes and methods of an object.

    Args:
        obj: The object to inspect.

    Returns:
        A list of strings representing the attributes
        and methods of the object.
    """
    return dir(obj)
