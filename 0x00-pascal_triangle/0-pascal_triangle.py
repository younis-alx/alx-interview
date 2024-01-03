#!/usr/bin/python3
"""
pascal_triangle
"""
def pascal_triangle(n):
    """
    returns a list of lists of integers representing the Pascal’s triangle of n:
    """
    if n <= 0:
        return []

    triangle = [[] for _ in range(n)]

    for row in range(n):
        for col in range(row + 1):
            if col == 0 or col == row:
                triangle[row].append(1)
            else:
                triangle[row].append(triangle[row - 1][col - 1] + triangle[row - 1][col])

    return triangle