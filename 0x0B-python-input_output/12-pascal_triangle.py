#!/usr/bin/python3
# 12-pascal_triangle.py

"""Defines a Pascal's Triangle function."""


def pascal_triangle(n):
    """pascal_triangle
    Args:
        n (int): number
    Returns:
        [list]: list of lists of integers representing
        the Pascal’s triangle of n
    """
    if n <= 0:
        return ""

    triangle = [[1]]
    for current_row in range(1, n):
        row = [1]
        prev_row = triangle[current_row - 1]
        for elem in range(1, current_row):
            row.append(prev_row[elem] + prev_row[elem - 1])
        row.append(1)
        triangle.append(row)
    return (triangle)
