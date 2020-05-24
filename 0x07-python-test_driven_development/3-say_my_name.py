#!/usr/bin/python3
"""
Module say_my_name
module that prints  My name is <first name> <last name>
Return: Nothing
"""


def say_my_name(first_name, last_name=""):
    """
    Function that prints  My name is <first name> <last name>
    Args:
        first_name: First name given to function
        last_name: Last name given to function

    Returns: Nothing

    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    elif not isinstance(last_name, str):
        print("last_name must be a string")
    else:
        print("My name is {} {}".format(first_name, last_name))
