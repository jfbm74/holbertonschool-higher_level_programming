#!/usr/bin/python3
"""
Module of Base Class
"""


class Base:
    """
    Base class
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initialize an instance
        :param id: Id object
        :type id: int
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
