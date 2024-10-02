#!/usr/bin/python3
"""
This module defines the CustomObject class which allows creating,
serializing, and deserializing custom objects.
"""


import pickle


class CustomObject:
    """
    A custom class with name, age, and student status attributes.
    This class can be serialized and deserialized.
    """
    def __init__(self, name, age, is_student):
        """
        Initialize a new CustomObject.

        Args:
            name (str): The name of the object.
            age (int): The age of the object.
            is_student (bool): Indicates whether the object is a student or not.
        """
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """
        Display the attributes of the object.
        """
        print("Name: {}".format(self.name))
        print("Age: {}".format(self.age))
        print("Is Student: {}".format(self.is_student))

    def serialize(self, filename):
        """
        Serialize the object and save it to a file.

        Args:
            filename (str): The name of the file to save the object to.

        Returns:
            bool: True if serialization was successful, None otherwise.
        """
        try:
            with open(filename, "wb") as f:
                pickle.dump(self, f)
        except Exception as e:
            return None

    @classmethod
    def deserialize(cls, filename):
        """
        Deserialize an object from a file.

        Args:
            filename (str): The name of the file to load the object from.

        Returns:
            CustomObject: The deserialized object, or None if an error occurred.
        """
        try: 
            with open(filename, "rb") as f:
                return pickle.load(f)
        except (FileNotFoundError, pickle.UnpicklingError) as e:
            return None
