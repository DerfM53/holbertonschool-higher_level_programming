#!/usr/bin/python3
"""
This module provides a function to convert JSON strings to Python objects.

It utilizes the json module to deserialize JSON-formatted strings into
their corresponding Python data structures. This module is useful for
parsing JSON data received from external sources or stored in files.
"""


import json


def from_json_string(my_str):
    """
    Return deserialized my_str in python format
    """
    return json.loads(my_str)
