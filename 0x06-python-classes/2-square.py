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
