#!/usr/bin/python3
"""canUnlockAll determines if all boxes can be opened"""


def canUnlockAll(boxes):
    """
    Determines if all boxes can be opened.

    Args:
        boxes (list): A list of lists where each index contains a list of
        integers representing a box.

    Returns:
        True: if all boxes can be opened
        else False
    """
    n = len(boxes)
    visited = [False] * n
    visited[0] = True
    stack = [0]

    while stack:
        current_box = stack.pop()
        for key in boxes[current_box]:
            if key < n and not visited[key]:
                visited[key] = True
                stack.append(key)

    return all(visited)
