#!/usr/bin/python3
"""
This module create an instance of class MyList
"""


class MyList(list):
    """
    This class create an instance with empty list attribute
    this attribute list can modify of intance
    """

    def __init__(self):
        super().__init__()

    def print_sorted(self):
        """
        This method sort a list of instance
        """
        print(sorted(self))
