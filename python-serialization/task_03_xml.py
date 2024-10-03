#!/usr/bin/python3
"""
This module provides functions for serializing dictionaries to XML files
and deserializing XML files back to dictionaries.
"""


import xml.etree.ElementTree as ET
import json


def serialize_to_xml(dictionary, filename):
    """
    Serialize a dictionary to an XML file.

    Args:
        dictionary (dict): The dictionary to serialize.
        filename (str): The name of the XML file to create.

    Returns:
        bool: True if serialization was successful, False otherwise.
    """
    try:
        root = ET.Element("data")
        for key, value in dictionary.items():
            child = ET.SubElement(root, key)
            child.text = str(value)
        tree = ET.ElementTree(root)
        tree.write(filename)
        return True
    except Exception as e:
        return False


def deserialize_from_xml(filename):
    """
    Deserialize an XML file to a dictionary.

    Args:
        filename (str): The name of the XML file to deserialize.

    Returns:
        dict: The deserialized dictionary if successful, None otherwise.
    """
    try:
        tree = ET.parse(filename)
        root = tree.getroot()
        data_dict = {}
        for child in root:
            data_dict[child.tag] = child.text
        return data_dict
    except Exception as e:
        return None
