# https://www.acmicpc.net/problem/2588
import sys

num1 = sys.stdin.readline().rstrip()
num2 = sys.stdin.readline().rstrip()


while num2 > 0:
    output = 0
    num1_copied = num1
    while num1_copied > 0:
        output += num2 % (10 * num1_copied % 10)
        num1_copied = num1_copied // 10

    print(output)
