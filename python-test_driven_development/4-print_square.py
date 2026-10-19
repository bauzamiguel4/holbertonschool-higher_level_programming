#!/usr/bin/python3
"""
Defines a square printing function.
"""


def print_square(size):
    """
    Prints a square with the character #.
    size must be an integer >= 0.
    """
    if not isinstance(size, int) or isinstance(size, bool):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        print("#" * size)
