#!/usr/bin/python3
"""
This module contains SwimMixin, FlyMixin, and Dragon classes to demonstrate
mixins and modular behavior composition in Python.
"""


class SwimMixin:
    """
    A mixin class adding swimming capabilities.
    """

    def swim(self):
        """
        Prints the swimming action of the creature.
        """
        print("The creature swims!")


class FlyMixin:
    """
    A mixin class adding flying capabilities.
    """

    def fly(self):
        """
        Prints the flying action of the creature.
        """
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """
    A Dragon class that composes behavior from SwimMixin and FlyMixin.
    """

    def roar(self):
        """
        Prints the roar of the dragon.
        """
        print("The dragon roars!")
