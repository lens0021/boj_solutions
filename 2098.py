# https://www.acmicpc.net/problem/2098
import sys
from itertools import permutations


def brute_force(dis):
    number_of_vertices = len(dis)

    if number_of_vertices == 1:
        return 0
    elif number_of_vertices == 2:
        return dis[0][1] + dis[1][0]
    else:
        min_dis = float('inf')
        for prm in permutations(range(1, number_of_vertices)):
            value = dis[0][prm[0]]
            for i in range(1, number_of_vertices-1):
                value += dis[prm[i-1]][prm[i]]
            value += dis[prm[-1]][0]
            min_dis = min(min_dis, value)

        return min_dis


def convent_input(str):
    if str == '0':
        return float('inf')
    else:
        return int(str)


number_of_vertices = int(sys.stdin.readline())
dis = [list(map(convent_input, sys.stdin.readline().split()))
       for _ in range(number_of_vertices)]

print(brute_force(dis))
