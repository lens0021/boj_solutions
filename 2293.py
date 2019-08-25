# https://www.acmicpc.net/problem/2293
# The memory limit is up to 4000000 byte
# So max usable number of ingeters is 4000000

from sys import stdin, stdout


def partition(coins, sum):
    # p(0) = 1 by convention for recurrence relations
    partition = [1] + [0] * (sum)

    # !!! below is COPIED from https://www.acmicpc.net/source/14760575 !!!
    for coin_value in coins:
        for larger_values in range(coin_value, sum+1):
            partition[larger_values] += partition[larger_values-coin_value]

    return partition[-1]


FINAL_SUM = int(stdin.readline().split()[1])
COINS = [int(v) for v in stdin.read().splitlines()]
stdout.write(str(partition(COINS, FINAL_SUM)) + '\n')
