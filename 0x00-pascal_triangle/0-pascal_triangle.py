#!/usr/bin/python3
"""
pascal_triangle
"""
def pascal_triangle(n):
    if n <= 0:
        return []

    triangle = [[] for _ in range(n + 1)]

    for row in range(n + 1):
        for col in range(row + 1):
            if col == 0 or col == row:
                triangle[row].append(1)
            else:
                triangle[row].append(triangle[row - 1][col - 1] + triangle[row - 1][col])

    return triangle