#!/usr/bin/python3
"""MAKECHANGE"""


def makeChange(coins, total):
    """Determines the fewest number of coins needed to meet
    the given amoount"""
    if total <= 0:
        return 0
    coin = 0
    tmp = 0
    coins.sort(reverse=True)
    for i in coins:
        while coin < total:
            coin += i
            tmp += 1
        if coin == total:
            return tmp
        coin -= i
        tmp -= 1
    return -1
