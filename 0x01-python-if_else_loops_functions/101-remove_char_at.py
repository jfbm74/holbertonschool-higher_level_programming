#!/usr/bin/python3
def remove_char_at(str, n):
    if n < 0 or n > len(str):
        return str
    elif str == '':
    else:
        return str.replace(str[n], '')
