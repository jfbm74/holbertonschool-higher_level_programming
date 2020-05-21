#!/usr/bin/python3
""" this module create the class Square"""


class Square:
    """ Class Square constuctor method"""
    def __init__(self, size=0):
        """
        Initializes with size (no type/value verification)
        Arg
            size: size of the square
        """
        if not type(size) is int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """
        Calculates square area
        Returns: area

        """
        return self.__size ** 2

    @property
    def size(self):
        """
        getter function for size
        Returns:
            size of square
        """
        return self.__size

    @size.setter
    def size(self, val):
        """
        setter function for attribute size
        Args:
            val: Set value for __size
        Returns: Nothing
        """
        if type(val) is not int:
            raise TypeError("size must be an integer")
        if val < 0:
            raise ValueError("size must be >= 0")
            self.__size = val
