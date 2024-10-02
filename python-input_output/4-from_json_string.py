#!/usr/bin/python3

import json


def from_json_string(my_str):
    """
    Return deserialized my_str in python format
    """
    return json.loads(my_str)
