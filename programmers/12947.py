# https://programmers.co.kr/learn/courses/30/lessons/12947


def sum_of_digit(n, base=10):
    sum = 0
    while n > 0:
        sum += n % base
        n //= base

    return sum


def solution(x):
    return True if x % sum_of_digit(x) == 0 else False
