#!/usr/bin/python3
"""
This module defines a CustomObject class that can be serialized and
deserialized using the pickle module.
"""
import pickle


class CustomObject:
    """
    A custom class representing an individual with name, age, and student status,
    capable of pickling and unpickling itself.
    """

    def __init__(self, name, age, is_student):
        """
        Initializes the CustomObject.

        Args:
            name (str): The name of the person.
            age (int): The age of the person.
            is_student (bool): Whether the person is a student.
        """
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """
        Prints out the object's attributes.
        """
        print("Name: {}".format(self.name))
        print("Age: {}".format(self.age))
        print("Is Student: {}".format(self.is_student))

    def serialize(self, filename):
        """
        Serializes the current instance and saves it to the provided filename.

        Args:
            filename (str): The file to save the pickled object to.

        Returns:
            None if an exception occurs, otherwise implicitly returns None.
        """
        try:
            with open(filename, 'wb') as f:
                pickle.dump(self, f)
        except Exception:
            return None

    @classmethod
    def deserialize(cls, filename):
        """
        Loads and returns an instance of CustomObject from the provided filename.

        Args:
            filename (str): The file to load the pickled object from.

        Returns:
            An instance of CustomObject, or None if an exception occurs.
        """
        try:
            with open(filename, 'rb') as f:
                return pickle.load(f)
        except Exception:
            return None
