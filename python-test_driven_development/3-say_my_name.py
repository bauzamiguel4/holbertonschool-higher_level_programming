#!/usr/bin/python3
"""
Defines a name printing function.
"""


def say_my_name(first_name=None, last_name=""):
    """
    Prints My name is <first name> <last name>.
    Raises TypeError if first_name or last_name is not a string.
    """
    if first_name is None:
        raise TypeError("say_my_name() missing 1 required positional argument: 'first_name'")
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
