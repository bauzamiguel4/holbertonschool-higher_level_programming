#!/usr/bin/python3
"""
This module contains the CountedIterator class that extends an iterator
to keep track of the number of items iterated over.
"""


class CountedIterator:
    """
    An iterator wrapper that counts how many items have been fetched.
    """

    def __init__(self, iterable):
        """
        Initializes the CountedIterator with an iterable and a counter.
        """
        self.iterator = iter(iterable)
        self.counter = 0

    def __iter__(self):
        """
        Returns the iterator object itself.
        """
        return self

    def __next__(self):
        """
        Fetches the next item from the iterator, increments the counter,
        and returns the item.
        """
        item = next(self.iterator)
        self.counter += 1
        return item

    def get_count(self):
        """
        Returns the current number of items iterated over.
        """
        return self.counter
