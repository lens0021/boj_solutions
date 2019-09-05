# https://programmers.co.kr/learn/courses/30/lessons/42862


def solution(n, lost, reserve):
    for student in lost:
        if student in reserve:
            lost[lost.index(student)] = None
            reserve[reserve.index(student)] = None

    for student in lost:
        if student is None:
            continue
        elif student - 1 in reserve:
            reserve[reserve.index(student - 1)] = None
        elif student + 1 in reserve:
            reserve[reserve.index(student + 1)] = None
        else:
            n -= 1

    return n
