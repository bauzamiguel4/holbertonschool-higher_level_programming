#!/usr/bin/python3
"""
Defines a matrix division function.
"""


def matrix_divided(matrix=None, div=None):
    """
    Divides all elements of a matrix by div, rounded to 2 decimal places.
    Returns a new matrix.
    """
    err_matrix = "matrix must be a matrix (list of lists) of integers/floats"
    err_size = "Each row of the matrix must have the same size"

    if matrix is None or div is None:
        raise TypeError("matrix_divided() missing required arguments")

    if not isinstance(matrix, list):
        raise TypeError(err_matrix)

    row_len = None
    for row in matrix:
        if not isinstance(row, list):
            raise TypeError(err_matrix)
        if row_len is None:
            row_len = len(row)
        elif len(row) != row_len:
            raise TypeError(err_size)
        for x in row:
            if not isinstance(x, (int, float)) or isinstance(x, bool):
                raise TypeError(err_matrix)

    if not isinstance(div, (int, float)) or isinstance(div, bool):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = []
    for row in matrix:
        new_row = []
        for x in row:
            try:
                val = round(x / div, 2)
            except (OverflowError, ZeroDivisionError, ValueError):
                val = 0.0
            new_row.append(val)
        new_matrix.append(new_row)
    return new_matrix
