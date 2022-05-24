from collections import deque

M, N = map(int, input().split())
Q = deque()
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:
            Q.append((i, j))

while Q:
    x, y = Q.popleft()

    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]

        if nx < 0 or nx >= N or ny < 0 or ny >= M:
            continue
        if arr[nx][ny] != 0 or visited[nx][ny] >= 1:
            continue

        arr[nx][ny] = 1
        visited[nx][ny] = visited[x][y] + 1
        Q.append((nx, ny))

flag = 1
for i in range(N):
    for j in range(M):
        if arr[i][j] == 0:
            flag = 0

result = 0
if flag == 1:
    for i in range(N):
        for j in range(M):
            if visited[i][j] > result:
                result = visited[i][j]
    print(result)
else:
    print(-1)


"""
6 4
0 0 -1 0 0 0
0 0 1 0 -1 0
0 0 -1 0 0 0
0 0 0 0 -1 1
"""