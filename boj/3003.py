# https://www.acmicpc.net/problem/3003
print(' '.join(
    str(t[0] - t[1])
    for t in
    zip([1, 1, 2, 2, 2, 8], map(int, input().split()))
))
