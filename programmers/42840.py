# https://programmers.co.kr/learn/courses/30/lessons/42840


def solution(answers):
    # 1번 수포자가 찍는 방식: 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, ...
    # 2번 수포자가 찍는 방식: 2, 1, 2, 3, 2, 4, 2, 5, 2, 1, 2, 3, 2, 4, 2, 5, ...
    # 3번 수포자가 찍는 방식: 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, ...
    patterns = [
        [1, 2, 3, 4, 5],
        [2, 1, 2, 3, 2, 4, 2, 5],
        [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    ]
    score = [0, 0, 0]

    for i, ans in enumerate(answers):
        for pattern_index in range(3):
            p = patterns[pattern_index]
            if p[i % len(p)] == ans:
                score[pattern_index] += 1

    return sorted(
        i+1
        for i, s in enumerate(score)
        if s == max(score)
    )
