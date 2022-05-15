from collections import deque


N = int(input())
Q = deque()

graph = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * N for _ in range(N)]

dx = [-1, -1, -1, 0, 1, 1, 1, 0]
dy = [-1, 0, 1, 1, 1, 0, -1, -1]

count = 0
for i in range(N):
    for j in range(N):
        if graph[i][j] == 1 and visited[i][j] == 0:
            count += 1
            visited[i][j] = 1
            Q.append((i, j))

        while Q:
            cur = Q.popleft()
            x, y = cur[0], cur[1]

            for k in range(8):
                nx = x + dx[k]
                ny = y + dy[k]

                if nx < 0 or nx >= N or ny < 0 or ny >= N:
                    continue
                if graph[nx][ny] == 0 or visited[nx][ny] == 1:
                    continue

                visited[nx][ny] = 1
                Q.append((nx, ny))

print(count)




"""
7
1 1 0 0 0 1 0
0 1 1 0 1 1 0
0 1 0 0 0 0 0
0 0 0 1 0 1 1
1 1 0 1 1 0 0
1 0 0 0 1 0 0
1 0 1 0 1 0 0
"""