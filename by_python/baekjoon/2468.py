from collections import deque


dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def bfs(depth):
    count = 0
    Q = deque()
    for i in range(N):
        for j in range(N):
            if arr[i][j] <= depth or visited[i][j] == 1:
                continue
            count += 1
            visited[i][j] = 1
            Q.append((i, j))

            while Q:
                x, y = Q.popleft()

                for k in range(4):
                    nx = x + dx[k]
                    ny = y + dy[k]

                    if nx < 0 or ny < 0 or nx >= N or ny >= N:
                        continue
                    if arr[nx][ny] <= depth or visited[nx][ny] == 1:
                        continue

                    visited[nx][ny] = 1
                    Q.append((nx, ny))

    return count


N = int(input())

arr = [list(map(int, input().split())) for _ in range(N)]

max_value = 0
visited = [[0] * N for _ in range(N)]
# print(bfs(4))
for i in range(0, 101):
    visited = [[0] * N for _ in range(N)]
    max_value = max(max_value, bfs(i))
#
print(max_value)

"""
5
6 8 2 6 2
3 2 3 4 6
6 7 3 3 2
7 2 5 3 6
8 9 5 2 7
"""