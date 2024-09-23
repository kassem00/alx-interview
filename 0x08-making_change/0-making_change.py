#!/usr/bin/python3
"""
Given a pile of coins of different values,
determine the fewest number of coins needed to meet a given amount total
"""

def makeChange(coins, total):
    if total <= 0:
        return 0
    # Initialize the dp array with infinity for all amounts except 0
    dp = [float('inf')] * (total + 1)
    dp[0] = 0
    
    # Sort coins to start with the smallest one, making early termination possible
    coins.sort()

    # For each coin, update the dp array
    for coin in coins:
        for i in range(coin, total + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)
    
    # If dp[total] is still infinity, it means we couldn't make the total
    return dp[total] if dp[total] != float('inf') else -1
