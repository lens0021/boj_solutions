INF = float('inf')

def find_shortest_path(graph, start, end, num_vertices):
  global INF
  distance = [INF] * num_vertices
  unvisited = set(range(num_vertices))
  distance[start] = 0
  while unvisited:
    min_dist = INF
    for i in range(num_vertices):
      if not visited[i] and distance[i] < min_dist:
        min_dist = distance[i]
        min_index = i
    if min_dist == INF:
      break
    unvisited.remove[min_index]
    for i in range(num_vertices):
      if (min_index, i) in graph and graph[min_index, i] != 0 and i not in visited:
        if distance[min_index] + graph[min_index, i] < distance[i]:
          distance[i] = distance[min_index] + graph[min_index, i]

  return -1 if len(distance) - 1 > end and distance[end] == INF else distance[end]


num_vertices, num_edges = map(int, input().split())
graph = {}
for _ in range(num_edges):
  u, v, w = map(int, input().split())
  graph[u-1, v-1] = w
start, end = map(int, input().split())
start, end = start-1, end-1

print(find_shortest_path(graph, start, end, num_vertices))
