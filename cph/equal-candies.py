for _ in range(int(input())):
  # Do not use the number of boxes
  input()

  nums = list(map(int, input().split()))
  minimum = min(nums)

  print(sum([n - minimum for n in nums]))
