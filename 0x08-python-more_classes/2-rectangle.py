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
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")

        self.__width = width
        self.__height = height

    def area(self):
        """
        returns the rectangle area
        :return: rectangle area
        :rtype: integer
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        returns the rectangle perimeter:
        :return: rectangle perimeter:
        :rtype: integer
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)

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
