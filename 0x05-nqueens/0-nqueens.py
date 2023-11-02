#!/usr/bin/python3
"""N-queens puzzle"""
import sys


def is_safe(board, row, col):
    """ Check the column on top of the current position"""
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True


def solve_nqueens(n):
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    def solve(board, row):
        if row == n:
            solutions.append(list(board))
            return

        for col in range(n):
            if is_safe(board, row, col):
                board[row] = col
                solve(board, row + 1)

    solutions = []
    board = [-1] * n
    solve(board, 0)

    return solutions


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    solutions = solve_nqueens(N)

    if solutions:
        for solution in solutions:
            for row in solution:
                print(f"[{solution.index(row)}, {row}]", end=' ')
            print()
    else:
        print("No solutions found for N =", N)
