#!/usr/bin/python3
"""
Create a pascal triangle
"""


def pascal_triangle(n):
    """
    returns a list of lists of integers representing the Pascal triangle of n
    """
    triangle = []
    for i in range(1, n+1):
        triangle.append(pascal_row(i))
    return triangle


def pascal_row(row_num):
    """
    Creates a pascal row value given an integer
    eg 1 -> 1
    2 -> 1 1
    3 -> 1 2 1
    """
    row = []
    if row_num <= 0:
        return []
    for i in range(row_num):
        if i == 0 or i == row_num-1:
            row.append(1)
        else:
            prev_row = pascal_row(row_num-1)
            row.append(prev_row[i-1] + prev_row[i])
    return row
