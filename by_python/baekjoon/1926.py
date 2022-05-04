from collections import deque

painting_count = 0
max_paint = 0


def bfs():
    global max_paint
    global painting_count
    queue = deque()
    size = 0

    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    for i in range(n):
        for j in range(m):
            if paint[i][j] == 1 and visited[i][j] != 1:
                visited[i][j] = 1
                queue.append((i, j))
                painting_count += 1
                size = 1
            else:
                continue
            while queue:
                cur_x, cur_y = queue.popleft()
                for a in range(4):
                    nx, ny = cur_x + dx[a], cur_y + dy[a]

                    if nx < 0 or nx >= n or ny < 0 or ny >= m:
                        continue
                    if paint[nx][ny] != 1 or visited[nx][ny] == 1:
                        continue

                    visited[nx][ny] = 1
                    queue.append((nx, ny))
                    size += 1
            max_paint = max(max_paint, size)


n, m = map(int, input().split())
paint = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]
bfs()

print(painting_count)
print(max_paint)
