#!/usr/bin/python3

"""
Checks if all locks has corresponding keys
@boxes: list of lists

Returns: Boolean
 O(n+m)
"""


def canUnlockAll(boxes):
    """
    returns boolean whether all boxes can be opened
    """
    visited = set()
    queue = [0]
    while queue:
        box = queue.pop(0)
        visited.add(box)
        for key in boxes[box]:
            if key not in visited:
                queue.append(key)
    return len(visited) == len(boxes)

