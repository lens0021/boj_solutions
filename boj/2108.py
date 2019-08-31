# https://www.acmicpc.net/problem/2108
from sys import stdin
from collections import Counter
from math import inf


def mode(lst: list):
    if len(lst) == 1:
        return lst[0]

    most_common = Counter(lst).most_common()

    if len(most_common) == 1 \
            or most_common[0][1] != most_common[0][1]:
        return most_common[0][0]

    # "여러 개 있을 때에는 최빈값 중 두 번째로 작은 값을 출력한다."
    srtlst = [e[0] for e in most_common if e[1] == most_common[0][1]]
    if len(srtlst) == 1:
        return srtlst[0]
    else:
        return srtlst[1]


LEN = int(stdin.readline())
NUMS = sorted(map(int, stdin.read().splitlines()))

sum = 0
min = inf
max = -inf
for num in NUMS:
    sum += num
    if num < min:
        min = num
    if num > max:
        max = num

AVERAGE = round(sum / LEN)
MEDIAN = NUMS[LEN//2]
MODE = mode(NUMS)
RANGE = max - min

print(
    AVERAGE,
    MEDIAN,
    MODE,
    RANGE,
    sep='\n'
)
