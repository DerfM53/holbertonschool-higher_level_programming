#!/usr/bin/python3
"""This module contain a class Student"""


class Student:
    """
    Make an instance of class Student with attribute
    first and last name and age
    """
    def __init__(self, first_name, last_name, age):
        """Make instance of classe student with this attribute"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Return object of attribute"""
        return {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "age": self.age
        }
