# https://www.acmicpc.net/problem/11399

from sys import stdin

length = int(input())
times = sorted(map(int, input().split()))

total = 0
for i, time in enumerate(times):
  total += (length - i) * time

print(total)
