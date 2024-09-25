#!/usr/bin/python3
"""
This module provides a function to
is_same_class attribute and methods of an object.
"""


def is_same_class(obj, a_class):
    """
    Return True if the type of obj is
    idently with a_class
    """
    return type(obj) is a_class
