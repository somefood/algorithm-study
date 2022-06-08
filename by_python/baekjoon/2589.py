from collections import deque

N, M = map(int, input().split())
arr = [list(input()) for _ in range(N)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

max_value = 0
Q = deque()
for i in range(N):
    for j in range(M):
        visited = [[-1] * M for _ in range(N)]
        if arr[i][j] == "W" or visited[i][j] != -1:
            continue
        visited[i][j] = 0
        Q.append((i, j))

        while Q:
            x, y = Q.popleft()

            for k in range(4):
                nx = x + dx[k]
                ny = y + dy[k]

                if nx < 0 or ny < 0 or nx >= N or ny >= M:
                    continue
                if arr[nx][ny] == "W" or visited[nx][ny] != -1:
                    continue

                visited[nx][ny] = visited[x][y] + 1
                Q.append((nx, ny))

            max_value = max(max_value, visited[x][y])


print(max_value)



"""
5 7
WLLWWWL
LLLWLLL
LWLWLWW
LWLWLLL
WLLWLWW
"""