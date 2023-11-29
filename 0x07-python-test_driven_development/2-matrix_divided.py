#!/usr/bin/python3
"""This is the matrix division documentation."""


def matrix_divided(matrix, div):
    """Divides all elements in the matrix by div"""
    if not isinstance(matrix, list):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")
    size = None
    for m in matrix:
        if not isinstance (m, list):
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats")
        if size is None:
            size = len(m)
        elif size != len(m):
            raise TypeError("Each row of the matrix must have the same size")
        for i in m:
            if not isinstance(i, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) of \
integers/floats")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [[round(i / div, 2) for i in m] for m in matrix]
