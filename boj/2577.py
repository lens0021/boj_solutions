# https://www.acmicpc.net/problem/2577
import sys

a, b, c = map(int, sys.stdin.read().split())
a = str(a * b * c)

counts = [a.count(dig)
  for dig in '0123456789']

counts = map(str, counts)

print('\n'.join(counts))
