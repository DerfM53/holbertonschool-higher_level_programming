#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for row in matrix:
        new_row = [element ** 2 for element in row]
        new_matrix.append(new_row)
    return new_matrix
