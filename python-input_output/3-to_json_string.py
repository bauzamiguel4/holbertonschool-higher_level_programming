#!/usr/bin/python3
"""
This module contains a function that returns the JSON
representation of an object (string).
"""
import json


def to_json_string(my_obj):
    """
    Returns the JSON string representation of a Python object.

    Args:
        my_obj: The Python object to serialize.

    Returns:
        str: The JSON string representation of the object.
    """
    return json.dumps(my_obj)
