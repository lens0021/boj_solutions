# https://www.acmicpc.net/problem/1261

from sys import stdin, stdout
from math import inf, isinf


def calculate_cost(maze: str, w: int, h: int) -> int:
    #
    # Use dijkstra algorithm
    #

    visited = [(0, 0)]
    visited_offset = 0
    distances = [inf for _ in range(w*h)]
    distances[0] = 0

    while True:
        # Choose unvisited vertex v with min distances[v]
        # print('\nvisited:', visited)
        dis, v = visited[visited_offset]
        visited_offset += 1
        print(f'{v} is choosen')

        # Refresh distances of the adjacencies
        for x, y in [
            (v % w, v//w-1),
            (v % w, v//w+1),
            (v % w-1, v//w),
            (v % w+1, v//w),
        ]:
            print(x, y)
            if x < 0 or x >= w or y < 0 or y >= h:
                continue
            print(x, y, w, h)

            passed_dis = dis + int(maze[x+y*w])

            if x == w - 1 and y == h - 1:
                return passed_dis

            if passed_dis < distances[x+y*w]:
                distances[x+y*w] = passed_dis
                if int(maze[x+y*w]) == 0:
                    visited.insert(visited_offset, (distances[x+y*w], x+y*w))
                else:
                    visited.append((distances[x+y*w], x+y*w))

        print('distances:', distances)

    return distances[-1]


WIDTH, HEIGHT = map(int, stdin.readline().split())
MAZE = stdin.read().replace('\n', '')
stdout.write(str(calculate_cost(MAZE, WIDTH, HEIGHT))+'\n')
