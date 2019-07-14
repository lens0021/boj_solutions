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


class BitSet:
    def __init__(self):
        self._int = 0

    @staticmethod
    def new_from_number(num):
        bit_set = BitSet()
        bit_set._int = num
        return bit_set

    def get(self, index):
        num = self._int
        num = num >> (index-1)
        return num & 1 == 1

    def set(self, index, value=True):
        num = 1 << index
        if value:
            self._int |= num
        else:
            self._int &= ~num

    def __str__(self):
        return bin(self._int)

    def indices_of_trues(self):
        index = 0
        num = self._int
        lst = []

        while num > 0:
            if num & 1 == 1:
                lst.append(index)
            num >>= 1
            index += 1

        return lst

    def not_all(self):
        return self._int == 0

    def copy(self):
        return BitSet.new_from_number(self._int)


NUMBER_OF_VERTICES = int(sys.stdin.readline())
distances = [
    [float('inf') if str == '0' else int(str)
     for str in sys.stdin.readline().split()]
    for _ in range(NUMBER_OF_VERTICES)
]


@lru_cache(None)
def min_weight_using_vertices(destination, usable_vertices: BitSet, rec_level=0):
    if usable_vertices.not_all():
        return distances[0][destination]

    sub_distances = {}
    for i in usable_vertices.indices_of_trues():
        if distances[i][destination] == 0:
            continue

        new_usable_vertices = usable_vertices.copy()
        new_usable_vertices.set(i, False)
        sub_distances[i] = min_weight_using_vertices(
            i, new_usable_vertices,
            rec_level+1
        ) + distances[i][destination]

    return min(sub_distances.values())


print(distances)
all_but_zero = BitSet.new_from_number(2 ** NUMBER_OF_VERTICES - 2)

# print(brute_force(distances))
print(min_weight_using_vertices(0, all_but_zero))
