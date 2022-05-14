# https://www.acmicpc.net/problem/2480

from sys import stdin
a, b, c = map(int, input().split())

A = a == b
B = a == c
C = b == c

score = A + B + C
if score == 3:
    print(10000 + a * 1000)
elif score == 1:
    if A:
        same = a
    elif B:
        same = a
    else:
        same = b
    print(1000 + same * 100)
else:
    print(max(a, b, c) * 100)


rate_of_x,
basic_of_y,
upper_of_y,
addition_of_y,
used = map(int, stdin.read().split())
