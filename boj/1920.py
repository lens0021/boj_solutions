# https://www.acmicpc.net/problem/1920
import sys

sys.stdin.readline()
arr = set(map(int, sys.stdin.readline().split()))

sys.stdin.readline()
numbers = map(int, sys.stdin.readline().split())
for num in numbers:
    if num in arr:
        print('1')
    else:
        print('0')
