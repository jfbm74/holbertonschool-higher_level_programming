#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    argc = len(sys.argv)
    if argc == 1:
        print("0 arguments.")
        exit()
    else:
        print("{} argument{}:".format(argc - 1, '' if argc == 2 else 's'))
        for i in range(1, argc):
            print("{}: {}".format(i, sys.argv[i]))
