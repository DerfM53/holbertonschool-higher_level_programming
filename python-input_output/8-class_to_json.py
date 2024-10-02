#!/usr/bin/python3
"""Module containt a function"""


def class_to_json(obj):
    """
    Return a dictionnary representative in
    json format
    """
    return obj.__dict__
