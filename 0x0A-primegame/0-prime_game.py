#!/usr/bin/python3
"""Prime game"""


def isWinner(x, nums):
    """Determines the winner of a prime game session with `x` rounds.
    """
    if x < 1 or not nums:
        return None

    # Generate primes using the Sieve of Eratosthenes up
    # to the maximum number in nums
    n = max(nums)
    primes = [True] * (n + 1)
    primes[0] = primes[1] = False

    for i in range(2, int(n ** 0.5) + 1):
        if primes[i]:
            for j in range(i * i, n + 1, i):
                primes[j] = False

    # Count the number of primes less than or equal to n for each round
    marias_wins, bens_wins = 0, 0
    for num in nums:
        primes_count = sum(primes[:num + 1])
        bens_wins += primes_count % 2 == 0
        marias_wins += primes_count % 2 == 1

    if marias_wins == bens_wins:
        return None
    return 'Maria' if marias_wins > bens_wins else 'Ben'
