#!/usr/bin/python3
"""
Rotate a 2D matrix 90 degrees clockwise in place.
"""

def rotate_2d_matrix(matrix):
    """
    Rotates a given NxN 2D matrix 90 degrees clockwise in place.
    :param matrix: 2D list of integers representing the matrix
    """
    for x in range(0, int(N / 2)):
        for y in range(x, N-x-1):
            temp = matrix[x][y]
            matrix[x][y] = matrix[y][N-1-x]
            matrix[y][N-1-x] = matrix[N-1-x][N-1-y]
            matrix[N-1-x][N-1-y] = matrix[N-1-y][x]
            matrix[N-1-y][x] = temp
