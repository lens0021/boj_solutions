num = int(input())
heights = [int(input()) for _ in range(num)]
equalTo = sum(heights) // num
print(sum([abs(equalTo - h) for h in heights])//2)
