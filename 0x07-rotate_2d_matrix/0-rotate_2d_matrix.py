#!/usr/bin/python3
"""
n*n 2D matrix, rotate it 90 degrees clockwise
"""


def rotate_2d_matrix(matrix):
    """
    Step 1: Transpose the matrix
    """
    n = len(matrix)
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    """
    Step 2: Reverse each row
    """
    for row in matrix:
        row.reverse()
