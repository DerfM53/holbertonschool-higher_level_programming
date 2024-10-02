#!/usr/bin/python3
"""This module contain a class Student"""


class Student:
    """
    Make an instance of class Student with attribute
    first and last name and age
    """
    def __init__(self, first_name, last_name, age):
        """Initialize instance of class Student with these attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Convert the object to a dictionary representation."""
        if attrs is None:
            return (self.__dict__)
        else:
            return ({attr: getattr(self, attr)
                     for attr in attrs if hasattr(self, attr)})

    def reload_from_json(self, json):
        """Replace all attributes of the Student instance."""
        for key, value in json.items():
            setattr(self, key, value)
