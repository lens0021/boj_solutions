# https://www.acmicpc.net/problem/4344
from sys import stdin
for line in stdin.read().splitlines()[1:]:
    nums = list(map(int, line.split()))

    num_of_people, total = nums[0], sum(nums[1:])
    sup = len([grade for grade in nums[1:] if total < num_of_people * grade])

    print('%.3f' % (sup / num_of_people * 100) + '%')
