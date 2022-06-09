from collections import deque

n, m = map(int, input().split())

arr = [list(map(int, list(input()))) for _ in range(n)]
visited = [[0] * m for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
Q = deque()

count = 0
for i in range(n):
    for j in range(m):
        if arr[i][j] == 1 or visited[i][j] == 1:
            continue
        count += 1
        visited[i][j] = 1
        Q.append((i, j))

        while Q:
            x, y = Q.popleft()
            for k in range(4):
                nx = x + dx[k]
                ny = y + dy[k]

                if nx < 0 or ny < 0 or nx >= n or ny >= m:
                    continue
                if arr[nx][ny] == 1 or visited[nx][ny] == 1:
                    continue

                visited[nx][ny] = 1
                Q.append((nx, ny))

print(count)

"""
15 14
00000111100000
11111101111110
11011101101110
11011101100000
11011111111111
11011111111100
11000000011111
01111111111111
00000000011111
01111111111000
00011111111000
00000001111000
11111111110011
11100011111111
11100011111111
"""