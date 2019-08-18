# https://www.acmicpc.net/problem/1254

from sys import stdin
import math


def solution(s):
    l = len(s)
    if s == s[::-1]:
        return l

    l2 = find_longerst_palindromic_substring_length(s)

    return l2 + (l - l2) * 2  # Returns l * 2 - 1 when l2 == 1


def find_longerst_palindromic_substring_length(s):
    max_length = 1
    for i in range(len(s)):
        for j in range(i+1, len(s)+1):
            if j != len(s):
                continue
            if s[i:j] == s[i:j][::-1]:
                print
                max_length = max(
                    max_length,
                    len(s[i:j])
                )

    return max_length


phrase = stdin.readline().rstrip()
print(solution(phrase))
