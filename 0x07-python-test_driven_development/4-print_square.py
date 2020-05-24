#!/usr/bin/python3
"""
Module print_square
This module prints a square with the character #
Return: Nothing
"""

def print_square(size):
    """
    Function print_square
    This function prints a square with the character #
    Args:
        size: is the size length of the square

    Returns: Nothing

    """

    if not isinstance(size, (int, float)):
        raise TypeError("size must be an integer")
    elif isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        for j in range(size):
            print("#", end="")
        print("")

    pass