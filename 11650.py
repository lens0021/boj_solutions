# https://www.acmicpc.net/problem/11650

from sys import stdin, stdout

stdout.write(
    '\n'.join(
        f'{v // 1000000 - 100000} {v % 1000000 - 100000}'
        for v
        in sorted(
            (v[0]+100000)*1000000 + v[1]+100000 for v in
            [
                tuple(map(int, line.split()))
                for line in stdin.read().splitlines()[1:]
            ]
        )
    ) + '\n'
)
