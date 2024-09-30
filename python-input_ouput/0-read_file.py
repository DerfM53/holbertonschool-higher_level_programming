#!/usr/bin/python3

def read_file(filename=""):
    """
    This function open and read filename in inpout
    an print the contain of file in ouput
    """
    with open(filename, encoding="utf-8") as f:
        read_data = f.read()
        print(read_data, end="")
