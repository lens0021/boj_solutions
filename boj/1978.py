# https://www.acmicpc.net/problem/1978

from math import sqrt
def is_prime(num):
  if num == 1:
    return False

  for divisor in range(2, int(sqrt(num))+1):
    if num % divisor == 0:
      return False

  return True

input()
print(
  len(
    [
      num for num
      in map(int, input().split())
      if is_prime(num)
    ]
  )
)
