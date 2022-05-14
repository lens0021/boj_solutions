# https://www.acmicpc.net/problem/11050

n, k = map(int, input().split())

# nCk = n! / ( k! * (n-k)! ) = (n(n-1)(n-2)…(n-k+1))/k!

dividend = 1
for a in range(n - k + 1, n + 1):
  dividend *= a
divisor = 1
for a in range(1, k + 1):
    divisor *= a

print(dividend // divisor)
