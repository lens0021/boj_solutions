# https://www.acmicpc.net/problem/2475
print(
    sum(
        num ** 2
        for num in map(int, input().split(' '))
    ) % 10
)
