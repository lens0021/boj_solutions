# https://www.acmicpc.net/problem/1181

from sys import stdin, stdout

stdout.write(
    '\n'.join(
        tp[1] for tp in
        sorted(
            (len(s), s)
            for s in
            set(stdin.read().splitlines()[1:])
        )
    )+'\n'
)
