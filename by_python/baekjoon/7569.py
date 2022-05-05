import sys
from collections import deque


def check_already(graph):
    for x in graph:
        for y in x:
            if all(y):
                pass
            else:
                return False
    return True


max_day = 0


def bfs():
    global max_day
    Q = deque()
    for z in range(h):
        for x in range(n):
            for y in range(m):
                if graph[z][x][y] == 1:
                    Q.append((z, x, y))

    while Q:
        cur_z, cur_x, cur_y = Q.popleft()

        for i in range(len(dx)):
            x = cur_x + dx[i]
            y = cur_y + dy[i]
            z = cur_z + dz[i]

            if 0 <= x < n and 0 <= y < m and 0 <= z < h:
                if graph[z][x][y] != 0:
                    continue
                graph[z][x][y] = graph[cur_z][cur_x][cur_y] + 1
                Q.append((z, x, y))
                max_day = max(max_day, graph[z][x][y])
    return max_day - 1


m, n, h = map(int, input().split())  # mn크기, h상자수
graph = []
queue = deque([])

for i in range(h):
    tmp = []
    for j in range(n):
        tmp.append(list(map(int, sys.stdin.readline().split())))
        for k in range(m):
            if tmp[j][k] == 1:
                queue.append([i, j, k])
    graph.append(tmp)

dx = [-1, 0, 1, 0, 0, 0]
dy = [0, 1, 0, -1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

if check_already(graph):
    print(0)
else:
    result = bfs()
    if check_already(graph):
        print(result)
    else:
        print(-1)