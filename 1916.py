# https://www.acmicpc.net/problem/1916

from sys import stdin

# Handle given conditions
number_of_nodes = int(stdin.readline())  # 1 <= N <= 1,000
number_of_edges = int(stdin.readline())  # 1 <= M <= 100,000

# Declare graph
graph = {}

# Store data into a graph
for _ in range(number_of_edges):
    src, dst, weight = map(int, stdin.readline().split())
    # weight is in [0, 100000]
    if src not in graph.keys():
        graph[src] = {}

    # See http://blog.naver.com/occidere/220919210992
    if dst not in graph[src].keys() or weight < graph[src][dst]:
        graph[src][dst] = weight

# Set path of each node to itself to zero
for vertex in range(1, number_of_nodes+1):
    if vertex not in graph.keys():
        graph[vertex] = {}
    graph[vertex][vertex] = 0

# Handle given conditions
source, destination = map(int, stdin.readline().split())

# Initialize for dijkstra algorithm
found = {source}
distance = {}
for vertex in range(1, number_of_nodes+1):
    if source in graph and vertex in graph[source]:
        distance[vertex] = graph[source][vertex]
    else:
        distance[vertex] = float('inf')


def choose():
    '''
    Choose shortest node that is not founded yet
    '''

    targets = set(range(1, number_of_nodes+1)) - found

    min_distance = float('inf')
    for vertex in targets:
        if distance[vertex] < min_distance:
            min_distance = distance[vertex]
            min_source = vertex

    return min_source


while destination not in found:
    shortest = choose()

    found |= {shortest}
    for vertex in graph[shortest].keys() - found:
        distance[vertex] = min(
            distance[shortest] + graph[shortest][vertex],
            distance[vertex]
        )


print(distance[destination])
