# https://www.acmicpc.net/problem/15552

from sys import stdin, stdout

for _ in range(int(stdin.readline())):
    stdout.write(
        str(
            sum(
                map(
                    int,
                    stdin.readline().split()
                )
            )
        ) + '\n'
    )
