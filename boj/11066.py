# https://www.acmicpc.net/problem/11066

from sys import stdin
from math import log2, floor


def min_cost(lst):
    l = len(lst)
    if l == 0:
        return 0
    if l == 1:
        return lst[0]
    p = floor(log2(l))
    if l == 2**p:
        rt = sum(lst)*p
    else:
        rt = sum(lst[:2**p])*p + min_cost(lst[2**p:])

    print(lst, '=>', rt, '|', p)
    return rt


lines = stdin.readlines()
for case in range(int(lines[0][0])):
    n = int(lines[case*2+1])
    sizes = list(map(int, lines[case*2+2].split(' ')))
    print(sizes)
    print(min_cost(sizes))

# print(min_cost([1, 3, 3, 4, 4, 5, 5, 5]))
