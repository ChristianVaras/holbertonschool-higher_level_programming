#!/usr/bin/python3
"""
Contains function that returns int lists of pascal triangle of any given size
"""


def pascal_triangle(n):
    if n <= 0:
        return []
    if n == 1:
        return [[1]]

    triangle = [[1]]
    for rows in range(n-1):
        l = [1]
        for i in range(rows):
            l.append(triangle[-1][i] + triangle[-1][i+1])
        l.append(1)
        triangle.append(l)
    return triangle
