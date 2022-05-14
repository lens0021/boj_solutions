# https://www.acmicpc.net/problem/10707

from sys import stdin

rate_x, basic_y, upper_y, extra_y, used = map(int, stdin.read().split())

fee_x = used * rate_x
if used <= upper_y:
  fee_y = basic_y
else:
  fee_y = basic_y + (used - upper_y) * extra_y

print(min(fee_x, fee_y))
