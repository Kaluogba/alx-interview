#!/usr/bin/python3
"""
This module provides a method to determine if all locked boxes can be opened.

"""


def canUnlockAll(boxes):
    """
    Determine if all locked boxes can be opened.

    Args:
        boxes (list of list of int): A list of lists representing the boxes.
            Each inner list contains the keys inside a box, where the index
            of the inner list represents the box number.

    Returns:
        bool: True if all boxes can be opened, False otherwise.

    Notes:
        - A key with the same number as a box opens that box.
        - The first box (boxes[0]) is unlocked by default.
        - You can assume all keys will be positive integers.
        - There can be keys that do not have boxes.

    Example:
        boxes1 = [[1], [2], [3], [4], []]
        print(canUnlockAll(boxes1))  # Output: True

        boxes2 = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
        print(canUnlockAll(boxes2))  # Output: True

        boxes3 = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
        print(canUnlockAll(boxes3))  # Output: False
    """
    if not boxes:
        return False

    n = len(boxes)
    visited = set()
    visited.add(0)  # The first box is unlocked by default
    queue = [0]     # Start with the keys from the first box

    while queue:
        current_box = queue.pop(0)
        for key in boxes[current_box]:
            if key < n and key not in visited:
                visited.add(key)
                queue.append(key)

    return len(visited) == n


# Test cases
if __name__ == "__main__":
    boxes1 = [[1], [2], [3], [4], []]
    print(canUnlockAll(boxes1))  # True

    boxes2 = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
    print(canUnlockAll(boxes2))  # True

    boxes3 = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
    print(canUnlockAll(boxes3))  # False
