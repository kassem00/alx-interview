#!/usr/bin/python3
"""
def pascal_triangle(n):
"""
"""
(x + y)^row
x=first element
y=last element

x^2 + xy + xy + y^2
"""


def pascal_triangle(n):
    """
    pascal_triangle that returns a list of lists of
    integers representing the Pascal’s triangle
    """
    if n == 0:
        return []
    if n == 1:
        return [[1]]

    triangle = [[1]]

    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            newElement = triangle[i-1][j-1] + triangle[i-1][j]
            row.append(newElement)
        row.append(1)
        triangle.append(row)

    return triangle
