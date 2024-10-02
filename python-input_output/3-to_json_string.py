#!/usr/bin/python3
"""
This module provides a function to convert Python objects to JSON strings.

It uses the json module to perform the serialization of Python objects
into their JSON string representation.
"""


import json


def to_json_string(my_obj):
    """
    Return serialized my_obj in json format
    """
    return json.dumps(my_obj)
