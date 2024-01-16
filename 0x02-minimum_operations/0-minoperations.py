#!/usr/bin/python3
'''
In a text file, there is a single character H.
 Your text editor can execute only two operations in this file:
   Copy All and Paste
'''


def minOperations(n):
    """
    minOperations
    Gets fewest # of operations needed to result in exactly n H characters
    """

    if (n < 2):
        return 0
    ops, root = 0, 2
    while root <= n:

        if n % root == 0:

            ops += root

            n = n / root

            root -= 1

        root += 1
    return ops
