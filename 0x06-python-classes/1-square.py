#!/usr/bin/python3
""" this module create the class Square"""


class Square:
    def __init__(self, size):
        """
        __init__ Square's Instantiation with size (no type/value verification)
        Args:
            size (): size of the square
        """
        self.__size = size
