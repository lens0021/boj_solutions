# https://www.acmicpc.net/problem/1934
from sys import stdin, stdout


def gcd(a, b):
    if a == b:
        return a
    if a == 0:
        return b
    if b == 0:
        return a
    if a > b:
        return gcd(b, a % b)
    if b > a:
        return gcd(a, b % a)


def lcm(a, b):
    return a*b // gcd(a, b)


stdout.write('\n'.join(
    str(lcm(*map(int, line.split(' '))))
    for line in stdin.readlines()[1:]
)+'\n')
