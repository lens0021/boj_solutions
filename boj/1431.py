# https://www.acmicpc.net/problem/1431

from sys import stdin, stdout

stdout.write('\n'.join(
    sorted(
        sorted(
            sorted(stdin.read().splitlines()[1:]),
            key=lambda code: sum(int(ch) for ch in code if ch.isdigit())
        ),
        key=len
    )
) + '\n')
