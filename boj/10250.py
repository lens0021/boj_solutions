# https://www.acmicpc.net/problem/10250
for _ in range(int(input())):
    H, _, N = map(int, input().split())
    print('%d%02d' % (((N - 1) % H) + 1, ((N - 1) // H) + 1))
