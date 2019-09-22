# https://www.acmicpc.net/problem/1022

DIRECTION = (
    (1, 0),
    (0, -1),
    (-1, 0),
    (0, 1)
)


MIN_X, MIN_Y, MAX_X, MAX_Y = map(int, input().split(' '))
_map = {}

num = 1
x, y = 0, 0
direction = 0
cnt = 0
while x < max(-MIN_X, MAX_X)+1 or y < max(-MIN_Y, MAX_Y)+1:
    for move in range(cnt//2 + 1):
        if MIN_X-2 <= x <= MAX_X+2 and MIN_Y-2 <= y <= MAX_Y+2:
            _map[x*10000+y] = num
        num += 1

        x += DIRECTION[direction][0]
        y += DIRECTION[direction][1]

    direction = (direction + 1) % 4
    cnt += 1

w = 1
for v in range(MIN_X, MAX_X+1):
    for u in range(MIN_Y, MAX_Y+1):
        if u*10000+v in _map:
            w = max(w, len(str(_map[u*10000+v])))


print('\n'.join(
    ' '.join([
        (str(_map[u*10000+v]).rjust(w)
         if u * 10000+v in _map
         else ' ' * w)
        for u in range(MIN_Y, MAX_Y+1)
    ])
    for v in range(MIN_X, MAX_X+1)
))
