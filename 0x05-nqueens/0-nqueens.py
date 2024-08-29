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
if __name__ == "__main__":
    dealing_with_user()
