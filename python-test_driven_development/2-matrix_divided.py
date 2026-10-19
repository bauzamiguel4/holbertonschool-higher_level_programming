#!/usr/bin/python3
"""
Defines a matrix division function.
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by div, rounded to 2 decimal places.
    Returns a new matrix.
    """
    err_matrix = "matrix must be a matrix (list of lists) of integers/floats"
    err_size = "Each row of the matrix must have the same size"

    if not isinstance(matrix, list) or not matrix:
        raise TypeError(err_matrix)

    row_len = None
    for row in matrix:
        if not isinstance(row, list) or not row:
            raise TypeError(err_matrix)
        if row_len is None:
            row_len = len(row)
        elif len(row) != row_len:
            raise TypeError(err_size)
        for x in row:
            if not isinstance(x, (int, float)):
                raise TypeError(err_matrix)

    if not isinstance(div, (int, float)) or isinstance(div, bool):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(x / div, 2) for x in row] for row in matrix]
