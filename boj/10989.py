# https://www.acmicpc.net/problem/10989

from sys import stdin, stdout

count_of_nums = [0] * (10000+1)

length = int(stdin.readline())
for _ in range(length):
    count_of_nums[int(stdin.readline())] += 1

for num in range(10000+1):
    stdout.write((str(num) + '\n') * count_of_nums[num])
