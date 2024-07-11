#!/usr/bin/python3
"""Calculates the fewest number of operations needed to result
exactly n H characters in the file"""


def minOperations(n):
    """Calculates the fewest number of operations needed to result
    exactly n H characters in the file"""
    if n <= 1:
        return 0
    operations = 0
    factor = 2
    while n > 1:
        while n % factor == 0:
            operations += factor
            n = n // factor
        factor += 1
    return operations
