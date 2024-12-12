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
        current_turn = 0  # 0 means Maria's turn, 1 means Ben's turn
        
        while primes:
            # The player whose turn it is picks the smallest prime number
            prime = primes.pop(0)
            # Remove the prime and all of its multiples from the set
            to_remove = set(range(prime, n + 1, prime))
            available_numbers -= to_remove
            
            # After the removal, check if there are still primes available to pick
            if not available_numbers:
                break
            # Switch turns
            current_turn ^= 1
        
        # If current_turn is 0, Maria won, otherwise Ben won
        if current_turn == 0:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
