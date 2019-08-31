# https://www.acmicpc.net/problem/14728
# 0-1 Knapsack Problem, See https://www.geeksforgeeks.org/0-1-knapsack-problem-dp-10/

from sys import stdin, stdout


def max_score(time_limit, sbjs):
    scores = [0] * (time_limit + 1)

    # reference: https://debuglog.tistory.com/106
    for sbj in sbjs:
        for time in range(time_limit, 0, -1):
            if sbj//10000 <= time and scores[time-sbj//10000] + sbj % 10000 > scores[time]:
                scores[time] = scores[time-sbj//10000] + sbj % 10000

    return scores[-1]


TIME_LIMIT = int(stdin.readline().split()[1])
SUBJECTS = [
    int(line.split()[0]) * 10000 + int(line.split()[1])
    for line in stdin.read().splitlines()
]

stdout.write(str(max_score(TIME_LIMIT, SUBJECTS)) + '\n')
