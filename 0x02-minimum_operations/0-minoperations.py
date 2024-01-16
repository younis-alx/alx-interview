#!/usr/bin/python3
'''
In a text file, there is a single character H.
 Your text editor can execute only two operations in this file:
   Copy All and Paste
'''


def minOperations(n):
    '''
    This method initializes a list
    dp to store the minimum number of operations for each number up to n
    '''
    dp = [0] + [float('inf')] * n
    for i in range(1, n + 1):
        for j in range(1, i // 2 + 1):
            if i % j == 0:
                dp[i] = min(dp[i], dp[j] + i // j)
    return dp[n] if n > 1 else 0
