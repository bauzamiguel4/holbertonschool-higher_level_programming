#!/usr/bin/python3
"""
This module contains a function that returns a list of lists of integers
representing the Pascal's triangle of n.
"""


def pascal_triangle(n):
    """
    Returns a list of lists of integers representing Pascal's triangle of n.

    Args:
        n (int): The number of rows of the triangle.

    Returns:
        list: A list of lists of integers.
    """
    if n <= 0:
        return []

    triangle = [[1]]
    for i in range(1, n):
        row = [1]
        last_row = triangle[-1]
        for j in range(1, i):
            row.append(last_row[j - 1] + last_row[j])
        row.append(1)
        triangle.append(row)

    return triangle
