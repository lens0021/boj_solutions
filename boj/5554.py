# https://www.acmicpc.net/problem/5554

from sys import stdin

time = sum(map(int, stdin.read().split()))
print(time//60, time % 60, sep='\n')
