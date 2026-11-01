#!/usr/bin/python3
"""
This module contains the abstract class Animal and its subclasses Dog and Cat.
"""
from abc import ABC, abstractmethod


class Animal(ABC):
    """
    An abstract class representing an animal.
    """

    @abstractmethod
    def sound(self):
        """
        Abstract method for animal sound.
        """
        pass


class Dog(Animal):
    """
    A class representing a dog, inheriting from Animal.
    """

    def sound(self):
        """
        Returns the sound of a dog.
        """
        return "Bark"


class Cat(Animal):
    """
    A class representing a cat, inheriting from Animal.
    """

    def sound(self):
        """
        Returns the sound of a cat.
        """
        return "Meow"
