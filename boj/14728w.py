# https://www.acmicpc.net/problem/14728
# 0-1 Knapsack Problem, See https://www.geeksforgeeks.org/0-1-knapsack-problem-dp-10/

from sys import stdin, stdout
from collections import namedtuple

Subject = namedtuple('Subject', ['time', 'score'])


def max_score(num_of_sbjs, time_limit, sbjs):
    scores = [
        [0 for _ in range(time_limit + 1)]
        for _ in range(num_of_sbjs + 1)
    ]

    for sbj in range(1, num_of_sbjs+1):
        for time in range(1, time_limit+1):
            if sbjs[sbj-1].time <= time:
                scores[sbj][time] = max(
                    scores[sbj-1][time-sbjs[sbj-1].time] +
                    sbjs[sbj-1].score,
                    scores[sbj-1][time]
                )

    return scores[-1][-1]


TIME_LIMIT = int(stdin.readline().split()[1])
SUBJECTS = sorted([
    subject
    for subject in [
        Subject(*map(int, line.split()))
        for line in stdin.read().splitlines()
    ]
    if subject.time <= TIME_LIMIT
], key=lambda t: t[1], reverse=True)

stdout.write(str(max_score(len(SUBJECTS), TIME_LIMIT, SUBJECTS)) + '\n')
