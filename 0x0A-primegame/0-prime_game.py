#!/usr/bin/python3
"""Prime Game
"""


def sieve_of_eratosthenes(n):
    """ Returns a list of prime numbers up to n using the Sieve of Eratosthenes. """
    primes = [True] * (n + 1)
    primes[0], primes[1] = False, False
    for i in range(2, int(n ** 0.5) + 1):
        if primes[i]:
            for j in range(i * i, n + 1, i):
                primes[j] = False
    return [i for i in range(2, n + 1) if primes[i]]

def isWinner(x, nums):
    """ Determine who wins the most rounds. """
    maria_wins = 0
    ben_wins = 0

    for n in nums:
        primes = sieve_of_eratosthenes(n)
        available_numbers = set(range(1, n + 1))
        turns = 0
        while primes:
            prime = primes.pop(0)
            for i in range(prime, n + 1, prime):
                if i in available_numbers:
                    available_numbers.remove(i)
            turns ^= 1
            if not available_numbers or not any(i in available_numbers for i in primes):
                break
        
        if turns == 0:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
