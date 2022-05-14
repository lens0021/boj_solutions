# https://www.acmicpc.net/problem/5543

print(
    min([int(input()) for _ in range(3)]) +
    min([int(input()) for _ in range(2)]) -
    50
)
