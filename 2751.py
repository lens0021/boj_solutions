# https://www.acmicpc.net/problem/2751

from sys import stdin, stdout

stdout.write(
    '\n'.join(
        map(
            str,
            sorted(
                map(
                    int,
                    stdin.read().splitlines()[1:]
                )
            )
        )
    ) + '\n'
)
