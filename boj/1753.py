# https://www.acmicpc.net/problem/1753
# 시간 제한은 기본 1초에 파이썬 보정으로 ×3+2되어 5초
import sys
from heapq import heappop, heappush

Debug = False


def log(msg, end='\n'):
    if Debug:
        print(msg, end=end)


number_of_verteces, number_of_edges = map(int, sys.stdin.readline().split())
source = int(sys.stdin.readline())

graph = {num: {num: 0} for num in range(1, number_of_verteces+1)}

for _ in range(number_of_edges):
    from_vertex, to_vertex, weight = map(int, sys.stdin.readline().split())

    if to_vertex not in graph[from_vertex].keys() or \
            weight < graph[from_vertex][to_vertex]:
        graph[from_vertex][to_vertex] = weight

log(f'그래프:{graph}')

costs = {num: float('inf') for num in range(1, number_of_verteces+1)}
costs[source] = 0
visit_heap = [(0, source)]

while visit_heap:
    log(len(visit_heap))
    # Choose vertex has min cost
    (min_cost, min_cost_vertex) = heappop(visit_heap)
    log(f'가장 짧은 거리({min_cost})를 가진 {min_cost_vertex}를 선택')
    log(f'그 인접 정점들({graph[min_cost_vertex]}) 중에서')

    # Recalculate
    for vertex in graph[min_cost_vertex]:
        if min_cost + graph[min_cost_vertex][vertex] < costs[vertex]:
            log(
                f'바로 {vertex}로 가는 것(비용:{costs[vertex]}) 대신'
                f'{min_cost_vertex}을(를) 경유하도록 갱신'
                f'(비용:{min_cost + graph[min_cost_vertex][vertex]})'
            )
            costs[vertex] = min_cost + \
                graph[min_cost_vertex][vertex]
            heappush(visit_heap, (costs[vertex], vertex))

for vertex in costs:
    if costs[vertex] == float('inf'):
        print('INF')
    else:
        print(costs[vertex])
