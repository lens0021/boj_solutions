# https://www.acmicpc.net/problem/9012

from sys import stdin, stdout

def is_vps(str):
    not_closed_parentheses = 0
    for ch in str:
        if ch == '(':
            not_closed_parentheses += 1
        else:
            not_closed_parentheses -= 1
            if not_closed_parentheses < 0:
                return False

    return True if not_closed_parentheses == 0 else False

_ = stdin.readline()

stdout.write('\n'.join([
    ('YES' if is_vps(line) else 'NO')
    for line in stdin.read().split()
])+'\n')
