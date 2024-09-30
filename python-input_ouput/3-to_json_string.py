#!/usr/bin/python3

import json


def to_json_string(my_obj):
    """
    Serialize my_obj and return file json format
    """
    json_string = json.dumps(my_obj)
    return json_string
