#!/usr/bin/python3
"""
This module contains the Shape abstract class, Circle and Rectangle subclasses,
and a shape_info function demonstrating duck typing.
"""
from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """
    An abstract base class representing a geometric shape.
    """

    @abstractmethod
    def area(self):
        """
        Abstract method to calculate the area of the shape.
        """
        pass

    @abstractmethod
    def perimeter(self):
        """
        Abstract method to calculate the perimeter of the shape.
        """
        pass


class Circle(Shape):
    """
    A class representing a circle, inheriting from Shape.
    """

    def __init__(self, radius=0):
        """
        Initializes a Circle instance.

        Args:
            radius (float/int): The radius of the circle.
        """
        self.radius = radius

    def area(self):
        """
        Calculates and returns the area of the circle.
        """
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        """
        Calculates and returns the perimeter (circumference) of the circle.
        """
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """
    A class representing a rectangle, inheriting from Shape.
    """

    def __init__(self, width=0, height=0):
        """
        Initializes a Rectangle instance.

        Args:
            width (float/int): The width of the rectangle.
            height (float/int): The height of the rectangle.
        """
        self.width = width
        self.height = height

    def area(self):
        """
        Calculates and returns the area of the rectangle.
        """
        return self.width * self.height

    def perimeter(self):
        """
        Calculates and returns the perimeter of the rectangle.
        """
        return 2 * (self.width + self.height)


def shape_info(shape):
    """
    Prints the area and perimeter of a shape object using duck typing.

    Args:
        shape: An object that implements area() and perimeter() methods.
    """
    print("Area: {}".format(shape.area()))
    print("Perimeter: {}".format(shape.perimeter()))
