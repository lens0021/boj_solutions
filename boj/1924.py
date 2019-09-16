# https://www.acmicpc.net/problem/1924

from datetime import date

WEEKDAYS = [
    "MON",
    "TUE",
    "WED",
    "THU",
    "FRI",
    "SAT",
    "SUN",
]
DAYS = [
    31,
    28,
    31,
    30,
    31,
    30,
    31,
    31,
    30,
    31,
    30,
    31
]

m, d = map(int, input().split())

print(WEEKDAYS[(sum(DAYS[: m-1])+d-1) % 7])
