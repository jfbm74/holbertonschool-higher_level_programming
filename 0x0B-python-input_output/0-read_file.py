#!/usr/bin/python3
"""
Module that reads a text file (UTF8) and prints it to stdout:
"""


def read_file(filename=""):
    """
    function that reads a text file (UTF8) and prints it to stdout:
    :param filename: Filename to read
    :type filename: filename
    :return: Text
    :rtype: String
    """
    with open("my_file_0.txt", "r", encoding='utf8') as f:
        for line in f:
            print(line, end="")
