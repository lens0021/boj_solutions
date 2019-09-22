# https://www.acmicpc.net/problem/2441

width = int(input())
print('\n'.join(
    ('*'*n).rjust(width)
    for n in range(width, 0, -1)
))
