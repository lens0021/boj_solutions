# https://www.acmicpc.net/problem/2588
import sys

num1 = int(sys.stdin.readline().rstrip())
num2 = int(sys.stdin.readline().rstrip())

for digit in str(num2)[::-1]:
  print(int(digit) * num1)

print(num1 * num2)
