#!/usr/bin/python3
"""  A method that determines if all the boxes can be opened."""


def canUnlockAll(boxes):
    """ A method that determines if all the boxes can be opened."""
    n = len(boxes)
    open_boxes = set([0])
    stack = [0]

    while stack:
        current_box = stack.pop()

        for key in boxes[current_box]:
            if key not in open_boxes and key < n:
                open_boxes.add(key)
                stack.append(key)

    return len(open_boxes) == n