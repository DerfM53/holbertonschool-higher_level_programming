#!/usr/bin/python3
"""
This module provides a function for appending text to a file.

It contains a single function, append_write, which allows users to
add text to the end of an existing file or create a new file if it
doesn't exist. The function is designed to work with UTF-8 encoded
text files.
"""


def append_write(filename="", text=""):
    """
    Open filename or create file if not create and add text
    in file and return the number of character.
    """
    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)
