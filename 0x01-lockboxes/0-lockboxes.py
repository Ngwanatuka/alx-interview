#!/usr/bin/python3
"""  A method that determines if all the boxes can be opened."""


def canUnlockAll(boxes):
    """ A method that determines if all the boxes can be opened."""
    n = len(boxes)
    reachable = [False] * n
    reachable[0] = True
    changed = True

    while changed:
        changed = False
        for i in range(n):
            if reachable[i]:
                for key in boxes[i]:
                    if not reachable[key]:
                        reachable[key] = True
                        changed = True

    return all(reachable)