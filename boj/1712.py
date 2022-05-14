# https://www.acmicpc.net/problem/1712

base, dynamic, price = map(int, input().split())

if price <= dynamic:
    print(-1)
else:
    print(base // (price - dynamic) + 1)
