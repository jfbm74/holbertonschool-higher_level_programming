#!/usr/bin/python3
"""
Module that returns the number of lines of a text file:
"""


def number_of_lines(filename=""):
    """
    function that returns the number of lines of a text file
    :param filename: File to read
    :type filename: filename
    :return: integer
    :rtype: int
    """
    counter = 0

    with open("my_file_0.txt", "r", encoding='utf8') as f:
        for line in f:
            counter += 1

    return counter
