#!/usr/bin/python3
"""
0-main
"""


def island_perimeter(grid):
    """
    island_perimeter
    """
    perimeter = 0

    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col] == 1:
                pram = 4
                max_left = len(grid[0])
                max_right = 0
                max_up = 0
                max_down = len(grid)

                # Check left
                if col != max_right:
                    if grid[row][col - 1] == 1:
                        pram -= 1

                # Check right
                if col != max_left:
                    if grid[row][col + 1] == 1:
                        pram -= 1

                # Check up
                if row != max_up:
                    if grid[row - 1][col] == 1:
                        pram -= 1

                # Check down
                if row != max_down:
                    if grid[row + 1][col] == 1:
                        pram -= 1

                perimeter += pram
    return perimeter
