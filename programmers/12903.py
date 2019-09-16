# https://programmers.co.kr/learn/courses/30/lessons/12903


def solution(s):
    l = len(s)
    return s[l//2-1:l//2+1] if l % 2 == 0 \
        else s[l//2]
