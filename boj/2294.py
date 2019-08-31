# https://www.acmicpc.net/problem/2294
# See https://www.geeksforgeeks.org/find-minimum-number-of-coins-that-make-a-change/

from sys import stdin, stdout

inf = 10001  # max value of coin defined in the problem is 10000


def min_length_partition(coins, sum):
    mins = [0] + [inf] * (sum)

    for value in range(1, sum+1):
        for coin in coins:
            if coin <= value and mins[value-coin] + 1 < mins[value]:
                mins[value] = mins[value-coin] + 1

    if mins[-1] == inf:
        return -1
    return mins[-1]


SUM = int(stdin.readline().split()[1])
COINS = sorted(
    # Remove duplications if there are
    set(
        value
        for value in map(int, stdin.read().splitlines())
        # Coins valued larger than the sum is useless
        if value <= SUM
    )
)

stdout.write(str(min_length_partition(COINS, SUM)) + '\n')
