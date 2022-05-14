# https://www.acmicpc.net/problem/5066
from sys import stdin

for line in stdin.read().splitlines()[:-1]:
  start, end = sorted(map(int, line.split()))
  counting = [0] * 10
  for num in range(start, end + 1):
    for digit in str(num):
      counting[int(digit)] += 1
  print(' '.join(map(str, counting)))
