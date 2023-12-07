#!/usr/bin/python3
"""
Module: Game of choosing Prime numbers
"""


def sieve_of_eratosthenes(n):
    """Return list of prime numbers between 1 and n inclusive
       Args:
        n (int): upper boundary of range. lower boundary is always 1
    """
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False

    for number in range(2, int(n**0.5) + 1):
        if is_prime[number]:
            for multiple in range(number * number, n + 1, number):
                is_prime[multiple] = False

    return [num for num in range(2, n + 1) if is_prime[num]]


def isWinner(x, nums):
    """
    Determines winner of Prime Game
    Args:
        x (int): no. of rounds of game
        nums (int): upper limit of range for each round
    Return:
        Name of winner (Maria or Ben) or None if winner cannot be found
    """
    if x is None or nums is None or x == 0 or not nums:
        return None

    Maria = Ben = 0

    for num in nums:
        prime_numbers = sieve_of_eratosthenes(num)
        if len(prime_numbers) % 2 == 0:
            Ben += 1
        else:
            Maria += 1

    return 'Maria' if Maria > Ben else ('Ben' if Ben > Maria else None)
