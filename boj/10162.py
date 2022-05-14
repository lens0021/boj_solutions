# https://www.acmicpc.net/problem/10162

t = int(input())
if t % 10:
  print(-1)
else:
  # we have buttons for 300, 60 and 10 sec.
  a = t // 300
  t %= 300
  b = t // 60
  t %= 60
  c = t //10
  print(a, b, c)
