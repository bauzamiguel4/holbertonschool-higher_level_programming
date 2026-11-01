#!/usr/bin/python3
"""
This module contains the function is_same_class.
"""


def is_same_class(obj, a_class):
    """
    Checks if an object is exactly an instance of a given class.

    Args:
        obj: The object to check.
        a_class: The class to check against.

    Returns:
        True if obj is exactly an instance of a_class, otherwise False.
    """
    return type(obj) is a_class
