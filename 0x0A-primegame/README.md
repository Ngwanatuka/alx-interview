# Prime Game

## Description

The __Prime Game__ is a program that simulates a game between two players, Maria and Ben. In each round, they take turns choosing a prime number from a set of consecutive integers starting from 1 up to and including *n*. The player who cannot make a move loses the game. The program determines the winner of each round and outputs the player with the most wins overall.

## Features

* The program uses dynamic programming to efficiently calculate prime numbers up to the specified __n__.
* The game is played optimally, assuming both players make the best possible moves.

## Usage

### Function Signature

```python
def isWinner(x, nums):
    """
    Determine the winner of each round and return the player with the most wins.

    Parameters:
    - x (int): The number of rounds.
    - nums (list): An array of `n` for each round.

    Returns:
    - str or None: The name of the player with the most wins. Returns `None` in case of a tie.
    """
    # Function implementation...
```

### Example

```python
from prime_game import isWinner

# Example usage
rounds = 3
numbers = [4, 5, 1]
winner = isWinner(rounds, numbers)
print(f"The winner is: {winner}")
```

## Requirements

* Python 3 or higher