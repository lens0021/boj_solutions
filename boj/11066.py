# https://www.acmicpc.net/problem/11066

from sys import stdin
from functools import lru_cache


@lru_cache(None)
def solution(case, left, right):
    ''' [left, right) '''
    l = right - left
    if l <= 1:
        rt = 0
    else:
        rt = min(
            solution(case, left, partition)
            + solution(case, partition, right)
            + sum(numbers[case][left:right])
            for partition in range(left+1, right)
        )
    return rt


lines = stdin.readlines()
number_of_testcases = int(lines[0][0])
numbers = [None for _ in range(number_of_testcases)]
output = ''
for case in range(number_of_testcases):
    length_of_numbers = int(lines[case*2+1])
    numbers[case] = list(map(int, lines[case*2+2].split(' ')))
    output += str(solution(case, 0, length_of_numbers))+'\n'

print(output, end='')
