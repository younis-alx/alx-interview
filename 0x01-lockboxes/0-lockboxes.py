#!/usr/bin/python3

"""
Checks if all locks has corresponding keys
@boxes: list of lists

Returns: Boolean
 O(n*m)
"""


def canUnlockAll(boxes):
    """
    returns boolean whether all boxes can be opened
    """
    keys = [0]
    for key in keys:
        for new_key in boxes[key]:
            if new_key not in keys and new_key < len(boxes):
                keys.append(new_key)
    return len(keys) == len(boxes)
