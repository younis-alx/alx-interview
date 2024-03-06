#!/usr/bin/python3
"""Island Perimeter Problem
"""


def island_perimeter(grid):
    """
    Calculates the perimeter of the island described in grid
    Args:
        grid: 2d list of integers containing 0(water) or 1(land)
    Return:
        the perimeter of the island
    """
    perimeter = 0

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 1:
                perimeter += calculate_cell_perimeter(grid, i, j)

    return perimeter


def calculate_cell_perimeter(grid, i, j):
    """
    Calculates the perimeter of a single cell in the island
    Args:
        grid: 2d list of integers containing 0(water) or 1(land)
        i: row index of the cell
        j: column index of the cell
    Return:
        the perimeter of the cell
    """
    cell_perimeter = 0

    if i <= 0 or grid[i - 1][j] == 0:
        cell_perimeter += 1
    if i >= len(grid) - 1 or grid[i + 1][j] == 0:
        cell_perimeter += 1
    if j <= 0 or grid[i][j - 1] == 0:
        cell_perimeter += 1
    if j >= len(grid[i]) - 1 or grid[i][j + 1] == 0:
        cell_perimeter += 1

    return cell_perimeter
