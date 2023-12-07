#!/usr/bi/python3
"""
Prime game
"""


def isWinner(x, nums):
    """
    Determine the winner of each round
     and return the player with the most wins.

    Parameters:
    - x (int): The number of rounds.
    - nums (list): An array of `n` for each round.

    Returns:
    - str or None: The name of the player with the most wins.
     Returns `None` in case of a tie.
    """
    def is_prime(num, primes):
        for p in primes:
            if p * p > num:
                break
            if num % p == 0:
                return False
        return True

    def count_primes(n, primes):
        count = 0
        for i in range(2, n + 1):
            if is_prime(i, primes):
                count += 1
        return count

    maria_wins = 0
    ben_wins = 0

    max_num = max(nums)
    sieve = [True] * (max_num + 1)
    sieve[0] = sieve[1] = False
    primes = []

    for i in range(2, int(max_num**0.5) + 1):
        if sieve[i]:
            primes.append(i)
            for j in range(i * i, max_num + 1, i):
                sieve[j] = False

    for n in nums:
        primes_count = count_primes(n, primes)
        if primes_count % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
