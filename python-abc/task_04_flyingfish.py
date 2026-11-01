#!/usr/bin/python3
"""
This module contains Fish, Bird, and FlyingFish classes to demonstrate
multiple inheritance and method resolution order (MRO).
"""


class Fish:
    """
    A class representing a fish.
    """

    def swim(self):
        """
        Prints the swimming action of a fish.
        """
        print("The fish is swimming")

    def habitat(self):
        """
        Prints the habitat of a fish.
        """
        print("The fish lives in water")


class Bird:
    """
    A class representing a bird.
    """

    def fly(self):
        """
        Prints the flying action of a bird.
        """
        print("The bird is flying")

    def habitat(self):
        """
        Prints the habitat of a bird.
        """
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """
    A class representing a flying fish, inheriting from both Fish and Bird.
    """

    def fly(self):
        """
        Prints the flying action of a flying fish.
        """
        print("The flying fish is soaring!")

    def swim(self):
        """
        Prints the swimming action of a flying fish.
        """
        print("The flying fish is swimming!")

    def habitat(self):
        """
        Prints the habitat of a flying fish.
        """
        print("The flying fish lives both in water and the sky!")
