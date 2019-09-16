from datetime import date
from calendar import monthrange
# https://programmers.co.kr/learn/courses/30/lessons/12901

WEEKDAYS = [
    "MON",
    "TUE",
    "WED",
    "THU",
    "FRI",
    "SAT",
    "SUN",
]


def solution(a, b):
    diff = sum(monthrange(2016, m)[1] for m in range(1, a))+b
    WEEKDAYS[(WEEKDAYS.index("FRI") + diff) % 7]
    return WEEKDAYS[date(2016, a, b).weekday()]
