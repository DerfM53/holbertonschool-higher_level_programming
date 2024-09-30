#!/usr/bin/python

def append_write(filename="", text=""):
    """
    Open filename or create file if not create and add text
    in file and return the number of character.
    """
    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)
