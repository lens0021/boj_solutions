# https://www.acmicpc.net/problem/11066

from sys import stdin, stdout, setrecursionlimit
from functools import lru_cache
setrecursionlimit(1000000)


def fast_sum(case, left, right):
    l = right - left
    if l == 0:
        return 0
    if left == 0:
        return sums[right]
    return sums[right] - sums[left-1]


@lru_cache(None)
def solution(case, left, right):
    ''' [left, right) '''
    l = right - left
    if l == 1:
        rt = 0
    elif l == 2:
        rt = numbers[case][left] + numbers[case][right-1]
    else:
        rt = min(
            solution(case, left, partition)
            + solution(case, partition, right)
            for partition in range(left+1, right)
        ) + fast_sum(case, left, right)
    return rt


lines = stdin.readlines()
number_of_testcases = int(lines[0])
numbers = [None for _ in range(number_of_testcases)]
output = ''
for case in range(number_of_testcases):
    length_of_numbers = int(lines[case*2+1])
    numbers[case] = list(map(int, lines[case*2+2].split(' ')))
    sums = [sum(numbers[case][:i+1]) for i in range(length_of_numbers)]
    print(sums)
    output += str(solution(case, 0, length_of_numbers))+'\n'

stdout.write(output)
