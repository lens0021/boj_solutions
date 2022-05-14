# https://www.acmicpc.net/problem/4673

def d(num):
  return num + sum([int(ch) for ch in str(num)])

is_self = [True for _ in range(10000)]

for num in range(1, 10000):
  if d(num) < 10000:
    is_self[d(num)] = False

print(*[i for i in range(1, 10000) if is_self[i]], sep='\n')
