from collections import deque

N = int(input())
arr = [list(map(int, input())) for _ in range(N)]
visited = [[0] * N for _ in range(N)]

Q = deque()
danji = list()
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

status = 1
for i in range(N):
    for j in range(N):
        if arr[i][j] == 1 and visited[i][j] == 0:
            count = 1
            visited[i][j] = status
            Q.append((i, j))

            while Q:
                x, y = Q.popleft()

                for k in range(4):
                    nx = x + dx[k]
                    ny = y + dy[k]

                    if nx < 0 or nx >= N or ny < 0 or ny >= N:
                        continue
                    if arr[nx][ny] == 0 or visited[nx][ny] >= 1:
                        continue

                    count += 1
                    visited[nx][ny] = status
                    Q.append((nx, ny))
            status += 1
            danji.append(count)


danji.sort()
for i in danji:
    print(i)

"""
7
0110100
0110101
1110101
0000111
0100000
0111110
0111000
"""