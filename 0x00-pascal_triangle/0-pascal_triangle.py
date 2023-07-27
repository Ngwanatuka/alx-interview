#!/usr/bin/python3
"""Pascal's Triangle"""


def pascal_triangle(n):
    """creation of a pascal triangle"""
    if n <= 0:
        return []

    traingle = [[1]]
    for i in range(1, n):
        prev_row = traingle[i-1]
        new_row = [1]
        for j in range(1, i):
            new_row.append(prev_row[j - 1] + prev_row[j])
        new_row.append(1)
        traingle.append(new_row)

    return traingle
