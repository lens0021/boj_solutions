# https://www.acmicpc.net/problem/10989

from sys import stdin, stdout

num_of_nums = [0] * (10000+1)

length = int(stdin.readline())
for _ in range(length):
    num_of_nums[int(stdin.readline())] += 1

for num, ct in enumerate(num_of_nums):
    for _ in range(ct):
        stdout.write(str(num)+'\n')
