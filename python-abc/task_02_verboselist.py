#!/usr/bin/python3
"""
This module contains the VerboseList class that extends the built-in list class
with notification messages on modification operations.
"""


class VerboseList(list):
    """
    A custom list class that prints notifications when items are
    appended, extended, removed, or popped.
    """

    def append(self, item):
        """
        Adds an item to the end of the list and prints a notification.
        """
        super().append(item)
        print("Added [{}] to the list.".format(item))

    def extend(self, iterable):
        """
        Extends the list with items from an iterable and prints a notification.
        """
        before_len = len(self)
        super().extend(iterable)
        added_count = len(self) - before_len
        print("Extended the list with [{}] items.".format(added_count))

    def remove(self, item):
        """
        Removes the first occurrence of an item and prints a notification.
        """
        print("Removed [{}] from the list.".format(item))
        super().remove(item)

    def pop(self, index=-1):
        """
        Pops an item at the given index and prints a notification.
        """
        item = self[index]
        print("Popped [{}] from the list.".format(item))
        return super().pop(index)
