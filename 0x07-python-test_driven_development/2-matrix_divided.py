#!/usr/bin/python3
"""
Module matrix_divided
module divide a matrix into given divisor
Return: new matrix
"""


def matrix_divided(matrix, div):
    """
    function that divides all elements of a matrix.
    Args:
        matrix: must be a list of lists of integers or floats
        div: number to divide each element of a matrix

    Returns: New matrix

    """

    if not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    rows = len(matrix)
    columns = len(matrix[0])
    new_matrix = [[0 for i in range(columns)] for i in range(rows)]

    for i in range(rows):
        if (len(matrix[i])) != columns:
            raise TypeError("Each row of the matrix must have the same size")
        for j in range(columns):
            if type(matrix[i][j]) != int and type(matrix[i][j]) != float:
                raise TypeError("matrix must be a matrix (list of lists) "
                                "of integers/floats")
            new_matrix[i][j] = round((matrix[i][j] / div), 2)
    return new_matrix
