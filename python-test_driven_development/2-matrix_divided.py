#!/usr/bin/python3
"""
This module contains a function that divides all elements of a matrix.
"""

def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a given number.

    Args:
        matrix (list of lists): The matrix to be divided.
        div (int or float): The number to divide the matrix elements by.

    Returns:
        list of lists: A new matrix with all elements divided by div,
                       rounded to 2 decimal places.

    Raises:
        TypeError: If matrix is not a list of lists of integers/floats,
                   if each row of the matrix doesn't have the same size,
                   or if div is not a number.
        ZeroDivisionError: If div is equal to 0.
    """
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    
    if len(matrix) == 0 or any(len(row) == 0 for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    
    row_length = len(matrix[0])
    if any(len(row) != row_length for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    
    if not all(isinstance(elem, (int, float)) for row in matrix for elem in row):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    
    if div == 0:
        raise ZeroDivisionError("division by zero")
    
    return [[round(elem / div, 2) for elem in row] for row in matrix]