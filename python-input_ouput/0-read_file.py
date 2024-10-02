#!/usr/bin/python3
"""
Module containing a function to read
and print the contents of a file.
"""


def read_file(filename=""):
    """
    Reads a text file (UTF8) and prints its contents to stdout.
    """
    with open(filename, encoding="utf-8") as f:
        read_data = f.read()
        print(read_data, end="")
