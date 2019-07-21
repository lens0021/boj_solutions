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

    def everything_is_false(self):  # 이거 영어로 뭐라 적어요
        return self._int == 0

    def copy(self):
        return BitSet.new_from_number(self._int)


NUMBER_OF_VERTICES = int(sys.stdin.readline())
DISTANCES = [
    [float('inf') if str == '0' else int(str)
     for str in sys.stdin.readline().split()]
    for _ in range(NUMBER_OF_VERTICES)
]


@lru_cache(None)
def min_weight_using_vertices(destination, usable_vertices: BitSet):
    if usable_vertices.everything_is_false():
        return DISTANCES[0][destination]

    sub_distances = []
    for i in usable_vertices.indices_of_trues():
        if DISTANCES[i][destination] == 0:
            continue

        new_usable_vertices = usable_vertices.copy()
        new_usable_vertices.set(i, False)
        sub_distances.append(
            min_weight_using_vertices(
                i, new_usable_vertices) + DISTANCES[i][destination]
        )

    return min(sub_distances)


def iteratively_find_min_weight():
    #      +---> 오른쪽 세 번째 비트가 0이므로 3번 정점을 사용하지 않는다는 뜻
    #      |+--> 오른쪽 두 번째 비트가 0이므로 2번 정점을 사용하지 않는다는 뜻
    #      ||+-> 오른쪽 첫 번째 비트가 1이므로 1번 정점을 사용한다는 뜻
    #      vvv
    # meme[001][n]은 1번 정점만을 사용하여 n번 정점으로 가는 최단 거리
    # meme[010][n]은 2번 정점만을 사용하여 n번 정점으로 가는 최단 거리
    # meme[011][n]은 1번과 2번 정점만을 사용하여 n번 정점으로 가는 최단 거리
    memo = [
        [
            float('inf')
            # 도착지로 사용할 수 있는 정점 수 만큼 초기화: [0, 1, 2, 3]
            for _ in range(NUMBER_OF_VERTICES)
        ]
        # 출발지이자 도착지인 0번 정점을 제외한 나머지를 사용할지 혹은 안 할지의 경우의 수만큼 초기화
        for _ in range(2**(NUMBER_OF_VERTICES-1))
    ]

    # memo[0]은 아무런 다른 정점을 거치지 않고 각 정점에 도달하는 최단거리이므로 그냥 그래프 각 간선의 가중치.
    for vertex in range(NUMBER_OF_VERTICES):
        memo[0][vertex] = DISTANCES[0][vertex]

    # Main procedure
    for bitset in range(1, 2**(NUMBER_OF_VERTICES-1)):
        # 비트셋이 나타내는 방문한 정점과 방문하지 않은 정점을 집합으로 구하기
        vertex = 0
        visited, unvisited = [], []
        for i in range(1, NUMBER_OF_VERTICES):
            if (bitset >> (i-1)) & 1:
                visited.append(i)
            else:
                unvisited.append(i)

        # 이 for문의 마지막에는 0번 정점(출발점)으로 가는 최단 거리도 계산시키기 위해 unvisited에 추가
        if bitset == 2**(NUMBER_OF_VERTICES-1)-1:
            unvisited.append(0)

        # print('bitset:', format(bitset, f'0{NUMBER_OF_VERTICES}b'), end=' ')
        # print('( visited:', visited, 'unvisited:', unvisited, ')')

        for destination in unvisited:
            # print(f'To go {destination}', end=' ')
            min_distance = float('inf')
            for waypoint in visited:
                # memo[011][3]을 구하기 위해서는 1번 정점을 경유하는 경우와 2번 정점을 경유하는 것 중 빠른 것을 구해야 하며
                # 즉 memo[001][2]+(2에서 3으로 가는 비용) 혹은 memo[010][1]+(1에서 3으로 가는 비용) 중 적은 것을 해야 한다
                # 아래는 위 예시에서 001과 010에 해당하는 비트셋.
                waypoint_bitset = bitset & ~(1 << (waypoint-1))
                # print(
                #     'using',
                #     waypoint, end='')
                # print(
                #     f' (memo[{format(waypoint_bitset,"03b")}][{waypoint}]({memo[waypoint_bitset][waypoint]})', end='+')
                # print(
                #     f'distance({DISTANCES[waypoint][destination]})', end='=')
                # print(
                #     f'{memo[waypoint_bitset][waypoint]+DISTANCES[waypoint][destination]})')
                min_distance = min(
                    min_distance,
                    memo[waypoint_bitset][waypoint] +
                    DISTANCES[waypoint][destination]
                )
            memo[bitset][destination] = min_distance

            # print(
            #     f'Set memo[{format(bitset, "03b")}][{destination}] to {memo[bitset][destination]}')
    # print(memo)
    return memo[-1][0]


# print(DISTANCES)

# print(brute_force(DISTANCES))
all_but_zero = BitSet.new_from_number(2 ** NUMBER_OF_VERTICES - 2)
# print(min_weight_using_vertices(0, all_but_zero))
print(iteratively_find_min_weight())
