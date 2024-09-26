#!/usr/bin/python3
"""
0-main
"""


def island_perimeter(grid):
    """
    island_perimeter
    """
    x: int= 0
    perimeter = 0

    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col] == 1:
                perimeter = perimeter + posetion(grid, row, col)
    return perimeter

def posetion(grid, row, column):
    """
    it looks around the element and find one
    every time it found 1 a round island it will -1
    from value of pram it asume first no one around island
    and return the pram
    nume calculated
    """
    pram = 4
    max_left = len(grid[0])
    max_right = 0
    max_up = 0
    max_down = len(grid)
    dirction = ['r', 'l', 'u','d']

    for d in dirction:
        if d == 'r':
             if column != max_right:
                 if grid[row][column - 1] == 1:
                     pram -= 1

        if d == 'l':
             if column != max_left:
                 if grid[row][column + 1] == 1:
                     pram -= 1

        if d == 'u':
            if row != max_up:
                 if grid[row -1][column] == 1:
                     pram -= 1
        if d == 'd':
            if row != max_down:
                 if grid[row + 1][column] == 1:
                     pram -= 1
    return pram
