#!/usr/bin/env python3
def no_c(my_string):
    new_str = ''
    for i in range(0, len(my_string)):
        if my_string[i] not in "Cc":
            new_str = new_str + my_string[i]
    return new_str
