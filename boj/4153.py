# https://www.acmicpc.net/problem/4153

from sys import stdin
for line in stdin.read().splitlines()[:-1]:
    nums = list(map(int, line.split()))
    index_of_max = nums.index(max(nums))
    if index_of_max != 2:
        nums[index_of_max], nums[2] = nums[2], nums[index_of_max]

    print('right' if nums[2]**2 == nums[0]**2 + nums[1]**2 else 'wrong')
