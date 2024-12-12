#!/usr/bin/python3
"""Prime Game
"""


def sieve_of_eratosthenes(n):
    """ Returns a list of prime numbers up to n using the Sieve of Eratosthenes. """
    primes = [True] * (n + 1)
    primes[0], primes[1] = False, False  # 0 and 1 are not primes
    for i in range(2, int(n ** 0.5) + 1):
        if primes[i]:
            for j in range(i * i, n + 1, i):
                primes[j] = False
    return [i for i in range(2, n + 1) if primes[i]]

def isWinner(x, nums):
    """ Determine who wins the most rounds. """
    maria_wins = 0
    ben_wins = 0

    # Loop through all rounds
    for n in nums:
        primes = sieve_of_eratosthenes(n)
        available_numbers = set(range(1, n + 1))
        turns = 0  # Maria starts first, so 0 means Maria's turn, 1 means Ben's turn
        
        while primes:
            # The player whose turn it is picks the smallest prime number
            prime = primes.pop(0)
            # Remove prime and its multiples from the set
            for i in range(prime, n + 1, prime):
                if i in available_numbers:
                    available_numbers.remove(i)
            # Switch turns
            turns ^= 1
        
            # If the set is empty or no primes left to pick, the current player loses
            if not available_numbers or not any(i in available_numbers for i in primes):
                break
        
        if turns == 0:  # If turns is 0 after the loop, Maria won
            maria_wins += 1
        else:  # If turns is 1, Ben won
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
