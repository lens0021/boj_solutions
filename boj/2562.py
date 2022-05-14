# https://www.acmicpc.net/problem/2562

from sys import stdin

nums = list(map(int, stdin.read().split()))
max_num = max(nums)

print(max_num, nums.index(max_num) + 1, sep='\n')
