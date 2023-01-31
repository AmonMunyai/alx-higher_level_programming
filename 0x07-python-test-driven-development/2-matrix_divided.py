#!/usr/bin/python3
"""Defines a function that divides all elements of a matrix."""


def matrix_divided(matrix, div):
    """Divide all elements of a matrix.

    Args:
        matrix (list): a list of lists of ints or floats.
        div (int/float): divisor.
    Raises:
        TypeError: if matrix contains non-numbers.
        TypeError: if matrix contains rows of different sizes.
        TypeError: if div is not an int or float.
        ZeroDivisionError: if div is 0.
    Returns:
        a new matrix of all elements divided by div,
        rounded to 2 decimal places.
    """
    msg = "matrix must be a matrix (list of lists) of integers/floats"
    if (not isinstance(matrix, list) or matrix == [] or
        not all(isinstance(row, list) for row in matrix) or
        not all(isinstance(num, int) or isinstance(num, float)
                for num in [num for row in matrix for num in row])):
        raise TypeError(msg)
    if (not all(len(row) == len(matrix[0]) for row in matrix)):
        raise TypeError("Each row of the matrix must have the same size")
    if (not isinstance(div, int) and not isinstance(div, float)):
        raise TypeError("div must be a number")
    if (div == 0):
        raise ZeroDivisionError("division by zero")
    return ([list(map(lambda x: round(x / div, 2), row)) for row in matrix])
