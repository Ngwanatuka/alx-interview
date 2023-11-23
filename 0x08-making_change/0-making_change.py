#!/usr/bin/python3
"""
    function that makes changes from within the function
"""


def makeChange(coins, total):
    """
    A function that determines the
    fewest number of coins needed to
    meet a given amount total
    """
    if total <= 0:
        return 0

    coins.sort(reverse=True)  # Sort coins in descending order
    coin_count = 0

    for coin in coins:
        # Use divmod to get the quotient and remainder
        num_coins, remaining_total = divmod(total, coin)

        coin_count += num_coins
        total = remaining_total

    return coin_count if total == 0 else -1
