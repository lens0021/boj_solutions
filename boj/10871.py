# https://www.acmicpc.net/problem/10871

from sys import stdin

mx = int(stdin.readline().split()[1]) # max
print(*[num for num in map(int, stdin.read().split(' ')) if num < mx])
