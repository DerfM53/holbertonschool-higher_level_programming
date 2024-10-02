#!/usr/bin/python3
"""
Module containing a function to read
and print the contents of a file.
"""


def read_file(filename=""):
    """
    Reads a text file (UTF8) and prints its contents to stdout.

    Args:
        filename (str): The name of the file to read. Defaults to an empty string.

    The function uses the 'with' statement to ensure proper file handling.
    It does not manage file permissions or handle exceptions for non-existent files.
    """
    with open(filename, encoding="utf-8") as f:
        read_data = f.read()
        print(read_data, end="")
