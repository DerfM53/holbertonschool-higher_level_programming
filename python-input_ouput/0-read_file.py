#!/usr/bin/python3
"""This module containt a function"""


def read_file(filename=""):
    """
    This function open and read filename in inpout
    an print the contain of file in ouput
    """
    with open(filename, "r" ,encoding="utf-8") as f:
        read_data = f.read()
        print(read_data, end="")
