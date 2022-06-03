from collections import deque

M, N, K = map(int, input().split())

arr = [[0] * N for _ in range(M)]
visited = [[0] * N for _ in range(M)]


for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())

    for i in range(min(y1, y2), max(y1, y2)):
        for j in range(min(x1, x2), max(x1, x2)):
            arr[i][j] = 1


dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

Q = deque()
result = []
count = 0
for i in range(M):
    for j in range(N):
        if arr[i][j] == 0 and visited[i][j] == 0:
            count = 1
            visited[i][j] = 1
            Q.append((i, j))

            while Q:
                cur_x, cur_y = Q.popleft()

                for a in range(4):
                    nx = cur_x + dx[a]
                    ny = cur_y + dy[a]

                    if nx < 0 or ny < 0 or nx >= M or ny >= N:
                        continue
                    if arr[nx][ny] == 1 or visited[nx][ny] == 1:
                        continue

                    visited[nx][ny] = 1
                    count += 1
                    Q.append((nx, ny))
            result.append(count)

result.sort()
print(len(result))
for x in result:
    print(x, end=" ")
