# https://www.acmicpc.net/problem/11720
from sys import stdin

print(sum(
    map(
        int,
        stdin.readlines()[1].strip()
    )
))
