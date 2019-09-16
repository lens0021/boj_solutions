# https://www.acmicpc.net/problem/1159
from sys import stdin, stdout

nums = {}
for name in stdin.read().splitlines()[1:]:
    if name[0] in nums:
        nums[name[0]] += 1
    else:
        nums[name[0]] = 1

if max(nums.values()) < 5:
    print('PREDAJA')
else:
    stdout.write(''.join(
        chr(order)
        for order in range(ord('a'), ord('z')+1)
        if chr(order) in nums and nums[chr(order)] >= 5
    )+'\n')
