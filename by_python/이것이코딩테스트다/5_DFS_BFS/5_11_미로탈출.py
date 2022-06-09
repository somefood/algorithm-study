from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

n, m = map(int, input().split())
arr = [list(map(int, input())) for i in range(n)]
visited = [[0] * m for _ in range(n)]

Q = deque()

Q.append((0, 0))
visited[0][0] = 1

while Q:
    x, y = Q.popleft()

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or ny < 0 or nx >= n or ny >= m:
            continue
        if arr[nx][ny] == 0 or visited[nx][ny] != 0:
            continue

        visited[nx][ny] = visited[x][y] + 1
        Q.append((nx, ny))

print(visited[n-1][m-1])

"""
5 6
101010
111111
000001
111111
111111
"""