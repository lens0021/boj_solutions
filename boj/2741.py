# https://www.acmicpc.net/problem/2741
from sys import stdin, stdout

stdout.write('\n'.join(
    map(
        str,
        range(1, int(stdin.read())+1)
    )
)+'\n')
