# https://www.acmicpc.net/problem/16673

(c, k, p) = map(int, input().split(' '))
print(sum(
    k * n + p * (n ** 2)
    for n in range(c+1)
))
