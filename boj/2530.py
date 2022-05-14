# https://www.acmicpc.net/problem/2530
h, m, s = map(int, input().split())
m = m + h * 60
s = s + m * 60

s += int(input())

print(
    s//60//60%24,
    s//60%60,
    s%60
)
