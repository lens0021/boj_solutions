# https://www.acmicpc.net/problem/2442

width = int(input()) * 2 - 1

for a in range(1, width, 2):
  print(' ' * ((width - a)//2), end='')
  print('*' * a)

for a in range(width , 0, -2):
  print(' ' * ((width - a) // 2), end='')
  print('*' * a)
