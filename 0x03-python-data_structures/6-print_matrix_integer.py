#!/usr/bin/python
def print_matrix_integer(matrix=[[]]):
    if matrix == [[]]:
        print("")
    else:
        for row in range(len(matrix)):
            for col in range(len(matrix[row])):
                if col == (len(matrix[row]) - 1):
                    print("{:d}".format(matrix[row][col]))
                else:
                    print("{:d}".format(matrix[row][col]), end=" ")
