#!/usr/bin/python3

"""
This Module provides a function to generate Pascal's triangle

"""


def pascal_triangle(n):
    """
    Generates Pascal's triangle up to the nth row.

    Args:
    - n (int): Number of rows in the triangle.

    Returns:
    - List of lists: Pascal's triangle up to the nth row.
    """
    if n <= 0:
        return []

    triangle = []
    for i in range(n):
        row = [1] * (i + 1)
        for j in range(1, i):
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
        triangle.append(row)

    return triangle


# Test cases
if __name__ == "__main__":
    test_cases = [5, 1, 0, 10, 100]
    for n in test_cases:
        print(f"Pascal's triangle for n = {n}:")
        triangle = pascal_triangle(n)
        for row in triangle:
            print(row)
        print()
