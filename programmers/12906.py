# https://programmers.co.kr/learn/courses/30/lessons/12906


def solution(arr):
    arr2 = []
    last = -1
    for e in arr:
        if e != last:
            arr2.append(e)
        last = e
    return arr2
