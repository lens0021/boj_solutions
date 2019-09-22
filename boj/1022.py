# https://www.acmicpc.net/problem/1022

DIRECTION = (
    (0, 1),
    (-1, 0),
    (0, -1),
    (1, 0),
)


r1, c1, r2, c2 = map(int, input().split(' '))
_map = {}

num = 1
r, c = 0, 0
direction = 0
cnt = 0
_max = max(abs(r1), abs(c1), abs(r2), abs(c2))+1
while r <= _max and c <= _max:
    for move in range(cnt//2 + 1):
        if r1 <= r <= r2 and c1 <= c <= c2:
            _map[r*10000+c] = num
        num += 1

        r += DIRECTION[direction][0]
        c += DIRECTION[direction][1]

    direction = (direction + 1) % 4
    cnt += 1

w = 1
for r in range(r1, r2+1):
    for c in range(c1, c2+1):
        if r*10000+c in _map:
            w = max(w, len(str(_map[r*10000+c])))

print('\n'.join(
    ' '.join([
        (
            str(_map[r*10000+c]).rjust(w)
            if r*10000 + c in _map
            else ' ' * w
        )
        for c in range(c1, c2+1)
    ])
    for r in range(r1, r2+1)
))
