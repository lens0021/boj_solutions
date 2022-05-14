# https://www.acmicpc.net/problem/8958
from sys import stdin

for st in stdin.read().split()[1:]:
  score = 0
  for cons in list(filter(None, st.split('X'))):
    ln = len(cons)
    score += ln * (ln + 1) // 2
  print(score)
