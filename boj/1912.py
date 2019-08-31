# https://www.acmicpc.net/problem/1912
from sys import stdin
from math import inf


def solution(iter) -> int:
    summary = -inf
    max_summary = -inf
    for num in iter:
        summary = max(
            summary + num,
            num
        )
        max_summary = max(summary, max_summary)

    return max_summary


stdin.readline()  # Unused
iter = map(int, stdin.readline().split())
print(solution(iter))
