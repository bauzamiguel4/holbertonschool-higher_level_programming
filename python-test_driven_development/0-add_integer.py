#!/usr/bin/python3
"""
Defines an integer addition function.
"""


def add_integer(a, b=98):
    """
    Adds two integers or floats.
    Casts floats to integers before addition.
    Raises TypeError if a or b is not an integer or float.
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    try:
        return int(a) + int(b)
    except (OverflowError, ValueError):
        raise TypeError("b must be an integer")
