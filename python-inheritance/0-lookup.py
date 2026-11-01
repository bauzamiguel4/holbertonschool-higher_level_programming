#!/usr/bin/python3
"""
This module contains the function lookup.
"""


def lookup(obj):
    """
    Returns the list of available attributes and methods of an object.

    Args:
        obj: The object to inspect.

    Returns:
        list: A list of string names of the object's attributes and methods.
    """
    return dir(obj)
