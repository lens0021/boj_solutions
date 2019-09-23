# https://www.acmicpc.net/problem/2338
from sys import stdin

(a, b) = map(int, stdin.read().split())
print('%d\n%d\n%d' % (a+b, a-b, a*b))
