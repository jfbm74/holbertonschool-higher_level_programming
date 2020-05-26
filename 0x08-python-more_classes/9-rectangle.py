#!/usr/bin/python3
"""
Class rectangle
"""


class Rectangle:
    """
    class Rectangle: Template for Rectangle objects
    """

    number_of_instances = 0
    print_symbol = "#"

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
        Rectangle.number_of_instances += 1

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

    def __str__(self):
        """
        return string representation of rectangle
        :return: string drawing a rectangle
        :rtype: str
        """
        my_str = ""

        my_str = my_str + "\n".join(str(self.print_symbol) * self.__width
                                    for j in range(self.__height))
        return my_str

    def __repr__(self):
        """
        Compute official representation of rectangle
        :return: representation of rectangle
        :rtype: str
        """
        rect_repr = "{}({}, {})".format(self.__class__.__name__, self.__width,
                                        self.__height)
        return rect_repr

    def __del__(self):
        """
        Delete an object
        :return: Nothing
        """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        returns the biggest rectangle based on the area
        :param rect_1:  an instance of Rectangle
        :type rect_1: Rectangle
        :param rect_2:  an instance of Rectangle
        :type rect_2: Rectangle
        :return: return the biggest rect or rect_1 if both have the same area
        :rtype: Rectangle
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """
        Returns a new Rectangle instance with width == height == size
        :param size: size of square
        """
        return cls(size, size)
