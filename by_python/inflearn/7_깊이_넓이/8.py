from collections import deque


n = int(input())

apple = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * n for _ in range(n)]


limit = n // 2
cnt = 0
hap = 0

queue = deque()

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

queue.append((n // 2, n // 2))
hap += apple[n//2][n//2]
visited[n//2][n//2] = 1

while queue:
    if cnt == limit:
        break
    size = len(queue)
    for i in range(size):
        cx, cy = queue.popleft()
        for j in range(4):
            nx = cx + dx[j]
            ny = cy + dy[j]

            if visited[nx][ny] != 0:
                continue

            hap += apple[nx][ny]
            visited[nx][ny] = 1

            queue.append((nx, ny))
    cnt += 1


print(hap)

"""
5
10 13 10 12 15
12 39 30 23 11
11 25 50 53 15
19 27 29 37 27
19 13 30 13 19
"""