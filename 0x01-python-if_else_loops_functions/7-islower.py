#!/usr/bin/env python3
def islower(c):
    tmp = ord(c)
    if tmp > 96 and tmp < 123:
        return True
    else:
        return False
