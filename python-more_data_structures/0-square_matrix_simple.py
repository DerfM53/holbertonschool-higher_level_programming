#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    def square_row(row):
        return list(map(lambda element: element ** 2, row))
    squared_rows = map(square_row, matrix)
    new_matrix = list(squared_rows)
    return new_matrix
