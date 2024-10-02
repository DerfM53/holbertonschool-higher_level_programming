#!/usr/bin/python3
"""
This module provides functionality to save Python objects to JSON files.

It contains a function that serializes a Python object to JSON format
and writes the resulting JSON string to a specified file. This module
is useful for persisting data structures in a format that is both
human-readable and easily parsed by other programs.
"""


import json


def save_to_json_file(my_obj, filename):
    """
    Serialized my_obj in json format and write in filename
    """
    with open(filename, 'w', encoding="utf-8") as f:
        json.dump(my_obj, f)
