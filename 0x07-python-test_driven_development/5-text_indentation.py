#!/usr/bin/python3
"""
Module text_indentation
This module prints a text with 2 new lines after each
of these characters: ., ? and :
Return: Nothing
"""


def text_indentation(text):
    """
    Function that prints a text with 2 new lines after each
    of these characters: ., ? and :
    Args:
        text:

    Returns: Nothing

    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    char = {".", "?", ":"}
    nl = 1

    for i in text:
        if i == " ":
            if nl == 1:
                continue
        else:
            nl = 0
        if i in char:
            print(i, end="")
            print("")
            print("")
            nl = 1
        else:
            print(i, end="")
            ln = 0
