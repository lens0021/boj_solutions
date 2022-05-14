# https://www.acmicpc.net/problem/1032

from sys import stdin

names = stdin.read().splitlines()[1:]

if len(names) == 1:
  print(names[0])
else:
  pattern = ''
  for i_ch in range(len(names[0])):
    same = True
    for i_name in range(1, len(names)):
      if names[0][i_ch] != names[i_name][i_ch]:
        same = False
        break
    pattern += names[0][i_ch] if same else '?'
  print(pattern)


