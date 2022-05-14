from heapq import heappop, heappush

lines = [*open(0)]
vertex_num, edge_num = map(int, lines[0].split())
start = int(lines[1])
graph = {}
for line in lines[2:]:
  s, e, w = map(int, line.split())
  if s not in graph or graph[s][0] > w:
    graph[s] = (e, w)

print(graph)

def dijkstra(graph, start):
  '''
  Uses dijkstra algorithm with priority queue
  '''
  dist = [float('inf')] * vertex_num
  dist[start] = 0
  queue = [(0, start)]
  while queue:
    d, v = heappop(queue)
    if dist[v] < d:
      continue
    (e, w) = graph[v]
    if dist[e] > dist[v] + w:
      dist[e] = dist[v] + w
      heappush(queue, (dist[e], e))
  return dist

print(dijkstra(graph, start))
