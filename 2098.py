# https://www.acmicpc.net/problem/2098
import sys
from functools import lru_cache
from itertools import permutations


def convert_input(str):
    if str == '0':
        return float('inf')
    else:
        return int(str)


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


def bool_list_to_int(lst):
    num = 0
    multiplier = 1
    for ele in lst:
        if ele:
            num += multiplier
        multiplier *= 2

    return num


def int_to_bool_list(num):
    lst = []
    while num > 0:
        lst.append(num % 2 == 1)
        num //= 2

    return lst


number_of_vertices = int(sys.stdin.readline())
dis = [list(map(convert_input, sys.stdin.readline().split()))
       for _ in range(number_of_vertices)]


@lru_cache(None)
def min_weight_using_vertices(destination, usable_vertices: int, rec_level=0):
    if usable_vertices == 0:
        return dis[0][destination]

    usable_vertices = int_to_bool_list(usable_vertices)

    sub_distances = {}
    for i, is_useable in enumerate(usable_vertices):
        if not is_useable:
            continue
        elif dis[i][destination] == 0:
            continue

        new_usable_vertices = usable_vertices.copy()
        new_usable_vertices[i] = False
        sub_distances[i] = min_weight_using_vertices(
            i, bool_list_to_int(new_usable_vertices),
            rec_level+1
        ) + dis[i][destination]

    return min(sub_distances.values())


# print(dis)
all_but_zero = [True for _ in range(number_of_vertices)]
all_but_zero[0] = False

# print(brute_force(dis))
print(min_weight_using_vertices(0, bool_list_to_int(all_but_zero)))
