#!/usr/bin/python3

import json


def save_to_json_file(my_obj, filename):
    """
    Serialized my_obj in json format and write in filename
    """
    with open(filename, 'a', encoding="utf-8") as f:
        f.write(json.dumps(my_obj))
