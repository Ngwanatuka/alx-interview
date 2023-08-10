#!/usr/bin/python3
""" Function that calculates the fewest number of operations needed to result """


def minOperations(n):
    """ Minimum operations """
    if n <= 1:
        return 0
    
    opertaions = 0
    current = 1
    buffer = 0

    while current < n:
        if n % current == 0:
            buffer = current
            current += buffer
            opertaions += 2
        else:
            current += buffer
            opertaions += 1
    return opertaions
