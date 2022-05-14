from heapq import heappush, heappop
from sys import stdin
from math import inf

# Handles the input
lines = stdin.read().splitlines()
vertex_num, edge_num, k, start = map(int, lines[0].split())
graph = [[] for _ in range(vertex_num)]
for line in lines[1:]:
  u, v = map(int, line.split())
  graph[u - 1].append(v - 1)

# Dijkstra's algorithm
heap = [(0, start - 1)]
dist = [inf for _ in range(vertex_num)]
dist[start - 1] = 0
while heap:
  current, current_dist = heappop(heap)
  for i in graph[current]:
    alt = current_dist + 1
    if dist[i] > alt:
      dist[i] = alt
      heappush(heap, (i, dist[i]))

# Prints the result
printed = False
for v, d in enumerate(dist):
  if d == k:
    print(v + 1)
    printed = True
if not printed:
  print(-1)
