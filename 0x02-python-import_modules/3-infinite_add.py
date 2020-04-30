#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    sum = 0
    val_arg = sys.argv
    argc = len(sys.argv)
    if argc > 1:
        for i in val_arg[1:]:
            sum = sum + int(i)
    print(sum)
