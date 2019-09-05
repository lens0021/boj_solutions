# https://programmers.co.kr/learn/courses/30/lessons/12909


def is_open(ch):
    return ch == "("


def is_close(ch):
    return ch == ")"


def solution(s):
    parentheses = 0

    for ch in s:
        if is_open(ch):
            parentheses += 1
        elif is_close(ch):
            if parentheses > 0:
                parentheses -= 1
            else:
                return False
    if parentheses:
        return False

    return True
