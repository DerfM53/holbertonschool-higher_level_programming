#!/usr/bin/python3
"""
This module provides functionality to load Python objects from JSON files.

It contains a function that reads a JSON-formatted file and deserializes
its contents into a Python object. This module is useful for retrieving
data structures that have been stored in JSON format, allowing easy
integration of persisted data back into Python programs.
"""


import json


def load_from_json_file(filename):
    """
    Take file format json et convert an python object
    """
    with open(filename, 'r', encoding="utf-8") as f:
        return json.load(f)
