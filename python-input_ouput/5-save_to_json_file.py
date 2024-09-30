#!/usr/bin/python3

import json


def save_to_json_file(my_obj, filename):
    """
    Serialized my_obj in json format and write in filename
    """
    with open(filename, 'w', encoding="utf-8") as f:
        json.dump(my_obj, f)
