#!/usr/bin/python3
def print_last_digit(number):

    multiple = 1
    x = number
    res = 0

    while x:
        if (x / 10) >= 1:
            x = x / 10
            multiple = multiple * 10
        else:
            break
    x = number
    while multiple >= 10:
        res = int(x / 10)
        x = x - (res * multiple)
        multiple = multiple / 10

    result = int(x)
    print("{}".format(result), end='')
    return result
