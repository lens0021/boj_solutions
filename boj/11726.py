# https://www.acmicpc.net/problem/11726

width = int(input())

if width == 1:
  cases = 1
elif width % 2 == 0:
  cases = (2 ** (width // 2))
else:
  squares = (width - 1) // 2
  cases = 2 ** squares * (squares - 1)


print(cases % 10007)
