#!/usr/bin/python3
"""
MyList class
"""


class MyList(list):
    """This is a subclass of list"""
    def __init__(self):
        """initializes the object"""
        super().__init__()

    def print_sorted(self):
        """print sorted list"""
        print(sorted(self))
