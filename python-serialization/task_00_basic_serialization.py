#!/usr/bin/python3
"""
This module provides basic serialization and deserialization functions
for working with JSON files and Python dictionaries.
"""


import json


def serialize_and_save_to_file(data, filename):
    """
    Serialize a Python dictionary to JSON and save it to a file.

    Args:
        data (dict): The Python dictionary to be serialized.
        filename (str): The name of the file to save the JSON data to.

    Returns:
        None
    """
    with open(filename, 'w', encoding="utf-8") as f:
        json.dump(data, f)


def load_and_deserialize(filename):
    """
    Load and deserialize JSON data from a file into a Python dictionary.

    Args:
        filename (str): The name of the file to load the JSON data from.

    Returns:
        dict: The deserialized Python dictionary.
    """
    with open(filename, 'r', encoding="utf-8") as f:
        data = json.load(f)
    return data
