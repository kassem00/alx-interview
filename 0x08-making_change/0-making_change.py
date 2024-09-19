#!/usr/bin/python3
"""
Given a pile of coins of different values,
determine the fewest number of coins needed to meet a given amount total
"""

def makeChange(coins, total):
    """ make change function """
    if total <= 0 or coin <= 0:
        return 0
