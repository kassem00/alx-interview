#!/usr/bin/python3
from typing import List
from sys import argv, exit


"""
N queens puzzle is the challenge of placing N
"""


def NQueens(N: int) -> List[List[str]]:
    """ N queens puzzle is the challenge of placing N """
    cds = set() #previce queen location 
    postDIG = set() # r-c = constant
    negtDIG = set() # r+c = constant

    for i in range(N):


        def NOT_D(row: int, col: int, previce_queen_location: dict) -> bool:
            """
            N queens puzzle is the challenge of placing N queens 
            in NxN squer
            this function return true 
            if location of quuen is not in danger with other quuens
            it will return false if it in danger
            """
            cds =set() #previce queen location
            postDIG = set() # r-c = constant
            negtDIG = set() # r+c = constant
            dead_row = set()
            dead_column = set()


def dealing_with_user() -> int:
    """ it will get data from user """
    list_from_user:list = argv

    if len(list_from_user) != 2:
        print("Usage: nqueens N")
        exit(1)
    try:
        num = int(list_from_user[1])
    except ValueError:
        print("N must be a number")
        exit(1)

    if num < 4:
        print("N must be at least 4")
        exit(1)
    return num


if __name__ == "__main__":
     num = dealing_with_user()
