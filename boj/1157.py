# https://www.acmicpc.net/problem/1157
counting = [0 for _ in range(ord('Z') - ord('A') + 1)]

for ch in input().upper():
  counting[ord(ch) - ord('A')] += 1

first = max(counting)

if counting.count(first) > 1:
  print('?')
else:
  print(chr(ord('A')+counting.index(first)))
