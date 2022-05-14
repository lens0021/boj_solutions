# https://www.acmicpc.net/problem/2884
hour, minute = map(int, input().split())
SUBSTRACTOR = 45

minute = hour * 60 + minute - 45
print(f'{minute//60%24} {minute%60}')
