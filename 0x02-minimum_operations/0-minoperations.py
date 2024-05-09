#!/usr/bin/python3
"""
Defines a method that calculates the fewest number of operations
needed to result in exactly n H characters in the file.
"""


def minOperations(n):
    """fewest number of operations needed to result in exactly n H characters.

    Args:
        n (int): The target number of H characters.

    Returns:
        int: The minimum number of operations required.

    """
    if n <= 1:
        return 0

    divisor = 2
    min_ops = 0

    # Perform prime factorization to calculate minimum operations
    while n > 1:
        if n % divisor == 0:
            n //= divisor
            min_ops += divisor
        else:
            divisor += 1

    return min_ops


if __name__ == "__main__":
    # Test cases
    n = 4
    print("Min # of operations to reach {} char: {}".format(
        n, minOperations(n)))

    n = 12
    print("Min # of operations to reach {} char: {}".format(
        n, minOperations(n)))
