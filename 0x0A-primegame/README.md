# Prime Game

This Python script simulates a game where two players, Maria and Ben, take turns choosing prime numbers from a set of consecutive integers. The goal is to determine the winner of each round based on optimal moves and gameplay.

## Usage

To use the script, you can import the `isWinner` function from the provided module (`0-prime_game.py`) and call it with the desired number of rounds and the list of integers for each round.

```python
#!/usr/bin/python3

from 0-prime_game import is_winner

print("Winner: {}".format(is_winner(5, [2, 5, 1, 4, 3])))
```

## Function

The `isWinner` function takes the number of rounds (x) and a list of integers (nums) as parameters and returns the name of the player who won the most rounds. If the winner cannot be determined, it returns `None`.

## Example

```python
print("Winner: {}".format(is_winner(5, [2, 5, 1, 4, 3])))
```
This will output the winner of each round based on the described gameplay.

## Note
* The script uses recursion and dynamic programming to optimize the calculation of the winner.
