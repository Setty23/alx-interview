#!/usr/bin/python3
"""Pascal's Triangle"""

 def pascal_triangle(n):
    """Returns a list of lists of integers
    representing the Pascal’s triangle of n:
    """
    if n <= 0:
        return []

    # Initialize the resulting array with n rows
    pascal = [[1] * (i + 1) for i in range(n)]

    for i in range(2, n):
        for j in range(1, i):
            pascal[i][j] = pascal[i - 1][j - 1] + pascal[i - 1][j]

    return pascal

# Example usage
if __name__ == "__main__":
    n = 5
    triangle = pascal_triangle(n)
    for row in triangle:
        print(row)
