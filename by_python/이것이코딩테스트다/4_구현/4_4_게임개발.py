from collections import deque

n, m = map(int, input().split())
x, y, d = map(int, input().split())

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
arr = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]

Q = deque()
visited[x][y] = 1
Q.append((x, y))
count = 1
while Q:
    cur_x, cur_y = Q.popleft()

    for i in range(4):
        nx = cur_x + dx[i]
        ny = cur_y + dy[i]

        if nx < 0 or ny < 0 or nx >= n or ny >= m:
            continue
        if arr[nx][ny] == 1 or visited[nx][ny] == 1:
            continue

        visited[nx][ny] = 1
        Q.append((nx, ny))
        count += 1

print(count)


"""
4 4
1 1 0
1 1 1 1
1 0 0 1
1 1 0 1
1 1 1 1
"""