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


def dealing_with_user() -> int:
    """ it will get data from user """
    list_from_user:list = argv

    if len(list_from_user) != 2:
        exit("Usage: nqueens N")

    if type(list_from_user[1] != int:
        exit("N must be a number")

    num = list_from_user[1]

    if num < 4:
        exit("N must be at least 4")
    return num


if __name__ == "__main__":
    print(dealing_with_user())
