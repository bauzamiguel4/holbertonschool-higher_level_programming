#!/usr/bin/python3
"""
This module contains the class MyList that inherits from the built-in list.
"""


class MyList(list):
    """
    A custom list class that inherits from list.
    """

    def print_sorted(self):
        """
        Prints the list in ascending sorted order without modifying the original.
        """
        print(sorted(self))
