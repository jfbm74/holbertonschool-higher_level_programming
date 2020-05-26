#!/usr/bin/python3
"""
Class rectangle
"""


class Rectangle:
    """
    class Rectangle: Template for Rectangle objects
    """

    def __init__(self, width=0, height=0):
        """
        Initialises a rectangle instantiation
        :param width: rectangle width
        :type width: int
        :param height: rectangle height
        :type height: int
        """
        self.__height = height
        self.__width = width

    @property
    def width(self):
        """
        Retrieve rectangle's width
        :return: __width
        :rtype: integer
        """
        return self.__width

    @property
    def height(self):
        """
        Retrieve rectangle's height
        :return: __height
        :rtype: integer
        """
        return self.__height

    @width.setter
    def width(self, value):
        """
        Set the value of width
        :param value: rectangles's width
        :type value: int
        :return: nothing
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """
        Set the value of height
        :param value: rectangle's height
        :type value: integer
        :return: nothing
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
