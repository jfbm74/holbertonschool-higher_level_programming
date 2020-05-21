#!/usr/bin/python3
""" this module create the class Square"""


class Square:
    """ Class Square constuctor method"""
    def __init__(self, size):
        """
        Initializes with size (no type/value verification)
        Arg
            size: size of the square
        """
        self.__size = size
