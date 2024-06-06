#!/usr/bin/python3
"""Making Change."""


def makeChange(coins, total):
    """Change comes from within."""
    if total < 1:
        return 0

    coins.sort()
    coins.reverse()

    count = 0

    for coin in coins:
        if total == 0:
            break

        unit_num = total // coin
        count += unit_num
        total -= (unit_num * coin)

    if total == 0:
        return count
    else:
        return -1
