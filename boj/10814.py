# https://www.acmicpc.net/problem/10814

from sys import stdin, stdout

users_by_age = [[] for _ in range(200+1)]

for line in stdin.read().splitlines(True)[1:]:
    users_by_age[int(line.split()[0])].append(line)

stdout.write(''.join(
    ''.join(u)
    for u in
    users_by_age
))
