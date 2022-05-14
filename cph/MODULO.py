nums = map(int,[*open(0)])
print(len(set([num % 42 for num in nums])))

