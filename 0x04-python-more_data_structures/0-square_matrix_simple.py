#!/usr/bin/python3
def newmat(matrix=[]):
    c = []
    for i in matrix:
        c.append(i ** 2)
    return c


def square_matrix_simple(matrix=[]):
    a = []
    for i in range(0, len(matrix)):
        a.append(newmat(matrix[i]))
    return a
