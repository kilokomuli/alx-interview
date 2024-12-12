#!/usr/bin/python3
""" Prime Game"""


def isWinner(x, nums):
    """
    Determine the winner of the prime number game.
    Args:
        x (int): Number of rounds.
        nums(list): List of n values for each round.
    Returns:
        str: Name of the player with the most wins ("Maria" or "Ben") or None.
    """
    if not nums or x <= 0:
        return None
    max_num = max(nums)
    sieve = [True] * (max_num + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(max_num**0.5) + 1):
        if sieve[i]:
            for multiple in range(i * i, max_num + 1, i):
                sieve[multiple] = False
    prime_count = [0] * (max_num + 1)
    for i in range(1, max_num + 1):
        prime_count[i] = prime_count[i - 1] + (1 if sieve[i] else 0)

    # Simulate the game for each n in nums
    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if prime_count[n] % 2 == 1:
            # Maria wins if the count of primes is odd
            maria_wins += 1
        else:
            # Ben wins if the count of primes is even
            ben_wins += 1

    # Determine the overall winner
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
