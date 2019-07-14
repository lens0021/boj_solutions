# https://www.acmicpc.net/problem/2098
import sys
from functools import lru_cache
from itertools import permutations


def brute_force(distances):
    NUMBER_OF_VERTICES = len(distances)

    if NUMBER_OF_VERTICES == 1:
        return 0
    elif NUMBER_OF_VERTICES == 2:
        return distances[0][1] + distances[1][0]
    else:
        min_dis = float('inf')
        for prm in permutations(range(1, NUMBER_OF_VERTICES)):
            value = distances[0][prm[0]]
            for i in range(1, NUMBER_OF_VERTICES-1):
                value += distances[prm[i-1]][prm[i]]
            value += distances[prm[-1]][0]
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


class BitSet:
    def __init__(self):
        self._int = 0

    def get(self, index):
        num = self._int
        num = num >> (index-1)
        return num & 1 == 1

    def set(self, index, value=True):
        num = 1 << index-1
        self._int |= num

    def __str__(self):
        return str(self._int)


NUMBER_OF_VERTICES = int(sys.stdin.readline())
distances = [
    [float('inf') if str == '0' else int(str)
     for str in sys.stdin.readline().split()]
    for _ in range(NUMBER_OF_VERTICES)
]


@lru_cache(None)
def min_weight_using_vertices(destination, usable_vertices: int, rec_level=0):
    if usable_vertices == 0:
        return distances[0][destination]

    usable_vertices = int_to_bool_list(usable_vertices)

    sub_distances = {}
    for i, is_useable in enumerate(usable_vertices):
        if not is_useable:
            continue
        elif distances[i][destination] == 0:
            continue

        new_usable_vertices = usable_vertices.copy()
        new_usable_vertices[i] = False
        sub_distances[i] = min_weight_using_vertices(
            i, bool_list_to_int(new_usable_vertices),
            rec_level+1
        ) + distances[i][destination]

    return min(sub_distances.values())


print(distances)
all_but_zero = [True for _ in range(NUMBER_OF_VERTICES)]
all_but_zero[0] = False

# print(brute_force(distances))
print(min_weight_using_vertices(0, bool_list_to_int(all_but_zero)))
