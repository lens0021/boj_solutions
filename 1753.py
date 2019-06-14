# https://www.acmicpc.net/problem/1753
import sys
from collections import namedtuple

Debug = False


def log(msg, end='\n'):
    if Debug:
        print(msg, end=end)


number_of_verteces, number_of_edges = map(int, sys.stdin.readline().split())
source = int(sys.stdin.readline())
graph = {}

for v in range(1, number_of_verteces+1):
    graph[v] = {v: 0}

for _ in range(number_of_edges):
    src, dst, weight = map(int, sys.stdin.readline().split())
    if src not in graph.keys():
        graph[src] = {}

    if dst not in graph[src].keys():
        graph[src][dst] = weight
    else:
        graph[src][dst] = min(
            graph[src][dst],
            weight
        )

log(graph)

distances = {}
FOUND = 0
DISTANCE = 1
for vertex in range(1, number_of_verteces+1):
    if vertex in graph[source]:
        distances[vertex] = [False, graph[source][vertex]]
    else:
        distances[vertex] = [False, float('inf')]

distances[source][FOUND] = True

while not all(distances[dst][FOUND] for dst in distances):
    log(distances)
    # Choose vertex has min distances
    min_distance_vertex = None
    min_distance = float('inf')

    for vertex in range(1, number_of_verteces+1):
        if not distances[vertex][0] and distances[vertex][1] < min_distance:
            min_distance = distances[vertex][1]
            min_distance_vertex = vertex

    # 선탁할 수 없는 정점이 없는 경우 종료
    if min_distance_vertex is None:
        break

    log(f'가장 짧은 거리({min_distance})를 가진 {min_distance_vertex}를 선택')
    distances[min_distance_vertex][FOUND] = True

    # Recalculate
    for vertex in distances:
        if distances[vertex][FOUND]:
            continue

        if vertex in graph[min_distance_vertex]:
            distances[vertex][DISTANCE] = min(
                min_distance + graph[min_distance_vertex][vertex],
                distances[vertex][DISTANCE]
            )

for vertex in distances:
    if distances[vertex][DISTANCE] == float('inf'):
        print('INF')
    else:
        print(distances[vertex][DISTANCE])
