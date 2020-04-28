#!/usr/bin/python3
def uppercase(str):
    largestr = len(str)
    for i in range(0, largestr):
        if ord(str[i]) >= 97 and ord(str[i]) <= 122:
            c = chr(ord(str[i]) - 32)
            print("{}".format(c), end='')
        else:
            print("{}".format(str[i]), end='')
    print("")
