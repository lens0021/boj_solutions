# https://www.acmicpc.net/problem/2845

line = input().split(' ')
area = int(line[0]) * int(line[1])
print(' '.join(
    str(v - area) for v
    in map(int, input().split(' '))
))
