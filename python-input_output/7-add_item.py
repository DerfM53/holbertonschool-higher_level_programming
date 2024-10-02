#!/usr/bin/python3
"""
This module create or add file format json if not create,
and add input arguments in this file and deserialized.
"""


import sys
import os
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"
if os.path.exists(filename):
    my_list = load_from_json_file(filename)
else:
    my_list = []

my_list.extend(sys.argv[1:])
save_to_json_file(my_list, filename)
