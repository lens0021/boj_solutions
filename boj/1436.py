# https://www.acmicpc.net/problem/1436
cnt = int(input())
nth = 0
while cnt:
    nth += 1
    if '666' in str(nth):
        cnt -= 1

print(nth)
