#!/usr/bin/python3
"""
This module contains the class MyInt that inherits from int.
"""


class MyInt(int):
    """
    A class that inherits from int but inverts the == and != operators.
    """

    def __eq__(self, other):
        """
        Inverts the == operator to behave like !=.
        """
        return super().__ne__(other)

    def __ne__(self, other):
        """
        Inverts the != operator to behave like ==.
        """
        return super().__eq__(other)
