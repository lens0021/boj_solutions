# https://www.acmicpc.net/problem/1260

DEBUG = False


def log(args, end='\n'):
    if DEBUG:
        print(args, end=end)


number_of_vertices, number_of_edges, starting_vertex = map(
    int, input().split())

graph = {}

for _ in range(number_of_edges):
    v1, v2 = map(int, input().split())

    # See https://www.acmicpc.net/board/view/19419
    if v1 > number_of_vertices or v2 > number_of_vertices:
        continue

    if v1 not in graph:
        graph[v1] = {}
    graph[v1][v2] = True

    if v2 not in graph:
        graph[v2] = {}
    graph[v2][v1] = True

log(graph)

if starting_vertex not in graph.keys():
    print(starting_vertex)
    print(starting_vertex)
    exit(0)

# DFS
visited = dict.fromkeys(graph, False)
job_stack = [starting_vertex]
output = []
while job_stack:
    log(f"스택{job_stack}에서", end=' ')
    vertex = job_stack.pop()
    log(f'{vertex}를 꺼내')

    if not visited[vertex]:
        log(f'{vertex}는 아직 방문하지 않았으니 출력하면서 방문한 걸로 표시하고')
        output.append(vertex)
        visited[vertex] = True

    log(
        f"{vertex}의 인접한 정점{list(graph[vertex].keys())} 중에서")
    for adjacency in sorted(graph[vertex], reverse=True):
        log(f'{adjacency}은', end=' ')
        if not visited[adjacency]:
            log('아직 방문하지 않았으니 스택에 추가하고')
            job_stack.append(adjacency)
        else:
            log('이미 방문했으니 말고')
    log(f'그러면 스택은 {job_stack}이 되는데')

print(' '.join(str(num) for num in output))

# BFS
visited = dict.fromkeys(graph, False)
visited[starting_vertex] = True
output = [starting_vertex]
job_queue = [starting_vertex]
while job_queue:
    log(f'큐{job_queue}에서', end=' ')
    vertex = job_queue.pop(0)
    log(f'{vertex}를 꺼내고')
    log(
        f"{vertex}의 인접한 정점{list(graph[vertex].keys())} 중에서")
    for adjacency in sorted(graph[vertex]):
        log(f'{adjacency}은', end=' ')
        if not visited[adjacency]:
            log('아직 방문하지 않았으니 스택에 추가하고', end=' ')
            visited[adjacency] = True
            log('출력한다')
            output.append(adjacency)
            job_queue.append(adjacency)
        else:
            log('이미 방문했으니 말고')

print(' '.join(str(num) for num in output))
