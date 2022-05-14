# https://www.acmicpc.net/problem/2798

the_num = int(input().split()[1])
nums = list(map(int, input().split()))
# nums = [num for num in nums if num <= the_num]
ln = len(nums)

total = 0
for i in range(ln):
  for j in range(i+1, ln):
    for k in range (j+1, ln):
      new_total = nums[i] + nums[j] + nums[k]
      if total < new_total <= the_num:
        total = new_total

print(total)
