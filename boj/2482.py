# https://www.acmicpc.net/problem/2482

whole, needed = int(input()), int(input())

dp = [[None for _ in range(1000 + 1)] for _ in range(1000 + 1)]

for i, v in enumerate(dp):
  v[0] = 1
  v[1] = i

for i in range(4, 1000 + 1):
  for j in range(1, i + 1):
    pass
