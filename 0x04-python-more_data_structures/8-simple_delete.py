#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    element = a_dictionary.pop(key, "error")
    if element == "error":
        pass
    return a_dictionary
