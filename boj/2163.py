# https://www.acmicpc.net/problem/2163
n, m = map(int, input().split())

how_many_times_break = [None for _ in range(n * m + 1)]

how_many_times_break[1] = 0

for i in range(2, n * m + 1):
  how_many_times_break[i] = 1 + how_many_times_break[i // 2] + how_many_times_break[i - i // 2]

print(how_many_times_break[-1])
