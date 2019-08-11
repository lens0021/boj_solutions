# https://www.acmicpc.net/problem/1912
from sys import stdin


def solution(iter) -> int:
    summary = float('-inf')
    max_summary = float('-inf')
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
