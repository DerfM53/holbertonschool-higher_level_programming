#!/usr/bin/python3
"""
This module contains a function to generate Pascal's triangle.
"""


def pascal_triangle(n):
    """
    Generates the first n rows of Pascal's triangle.

    Args:
        n (int): The number of rows of Pascal's triangle to generate.

    Returns:
        list: A list of lists representing Pascal's triangle.
              Each sublist represents a row of the triangle.
              Returns an empty list if n <= 0.

    Pascal's triangle is an arithmetic triangle where each number
    is the sum of the two numbers directly above it.
    """
    if n <= 0:
        return []
    triangle = [[1]]
    for i in range(1, n):
        ligne_precedente = triangle[-1]
        nouvelle_ligne = [1]
        for j in range(1, i):
            nouvelle_ligne.append(ligne_precedente[j-1] + ligne_precedente[j])
        nouvelle_ligne.append(1)
        triangle.append(nouvelle_ligne)
    return triangle
