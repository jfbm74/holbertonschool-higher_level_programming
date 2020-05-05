#!/usr/bin/python
def print_matrix_integer(matrix=[[]]):
    if matrix == [[]]:
        print("")   
    else:
        for row in range(len(matrix[0])):
            for col in range(len(matrix[0])):
                print("{:d}".format(matrix[row][col]), end=" ")
            print()
