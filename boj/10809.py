# https://www.acmicpc.net/problem/10809

st = input().strip()
answer = []

for ch in 'abcdefghijklmnopqrstuvwxyz':
  answer.append(st.index(ch) if ch in st else -1)

print(*answer)
