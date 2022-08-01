from collections import deque


def check_already(graph):
    for x in graph:
        if all(x):
            pass
        else:
            return False
    return True

max_day = 0


def bfs():
    global max_day
    Q = deque()
    for i in range(N):
        for j in range(M):
            if tomato[i][j] == 1:
                day = 1
                visited[i][j] = 1
                Q.append((i, j))
            elif tomato[i][j] == -1:
                visited[i][j] = 1
                continue
            else:
                continue
    while Q:
        cx, cy = Q.popleft()
        for k in range(4):
            x = cx + dx[k]
            y = cy + dy[k]

            if x < 0 or x >= N or y < 0 or y >= M:
                continue
            if tomato[x][y] != 0 or visited[x][y] != 0:
                continue

            tomato[x][y] = tomato[cx][cy] + 1
            visited[x][y] = 1
            Q.append((x, y))
            max_day = max(max_day, tomato[x][y])
    return max_day - 1


dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

M, N = map(int, input().split())

tomato = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]


if check_already(tomato):
    print(0)
else:
    result = bfs()
    if check_already(tomato):
        print(result)
    else:
        print(-1)

"""
6 4
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 1
"""