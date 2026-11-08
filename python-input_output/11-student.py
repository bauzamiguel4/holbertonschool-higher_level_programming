#!/usr/bin/python3
"""
This module contains a Student class that defines a student and
provides methods to serialize and deserialize its attributes.
"""


class Student:
    """
    A class that represents a student.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initializes a new Student instance.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student instance.
        If attrs is a list of strings, only retrieves those attributes.

        Args:
            attrs (list): Optional list of attribute names to retrieve.

        Returns:
            dict: The dictionary representation of the student.
        """
        if type(attrs) is list and all(type(attr) is str for attr in attrs):
            return {k: v for k, v in self.__dict__.items() if k in attrs}
        return self.__dict__

    def reload_from_json(self, json):
        """
        Replaces all attributes of the Student instance.

        Args:
            json (dict): A dictionary mapping attribute names to values.
        """
        for key, value in json.items():
            setattr(self, key, value)
