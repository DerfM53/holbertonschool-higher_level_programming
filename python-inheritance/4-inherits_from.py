#!/usr/bin/python3
"""
This module provides a function to
inherits_from attribute and methods of an object.
"""


def inherits_from(obj, a_class):
    """
    Return true if obj is an instance of subclasses inherite
    else return false
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
