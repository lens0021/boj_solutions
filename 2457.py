# https://www.acmicpc.net/problem/2457
from sys import stdin
from math import inf
from collections import namedtuple

START = 301
END = 1130


def date_to_number(month: int, day: int) -> int:
    # http://wookje.dance/2017/08/20/boj-2457-%EA%B3%B5%EC%A3%BC%EB%8B%98%EC%9D%98-%EC%A0%95%EC%9B%90/
    return month*100 + day


Rose = namedtuple('Rose', ['bloom', 'fall'])
lines = stdin.readlines()
roses = [None] * int(lines[0])
idx = 0
for line in lines[1:]:
    words = tuple(map(int, line.split()))
    bloom = date_to_number(words[0], words[1])
    fall = date_to_number(words[2], words[3])
    if fall < START or bloom > END \
            or bloom >= fall:  # https://www.acmicpc.net/board/view/1749#comment-5404
        continue
    roses[idx] = Rose(
        bloom=date_to_number(words[0], words[1]),
        fall=date_to_number(words[2], words[3])
    )
    idx += 1

roses.sort()

left = START
right = -inf
count = 0
while right <= END:
    unfound = True
    for rose in roses:
        if rose.bloom <= left and rose.fall > right:
            right = rose.fall
            unfound = False
    if unfound:
        print(0)
        exit(0)
    left = right
    count += 1

print(count)
