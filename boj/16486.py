# https://www.acmicpc.net/problem/16486
M = 1000000
PI = 3141592

d, r = [int(input()) for _ in range(2)]

anw = str(2*PI*r + d*2*M)
print(f'{anw[:-6]}.{anw[-6:]}')
