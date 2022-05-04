from collections import deque

normal = 0
abnormal = 0


def bfs():

    queue = deque()

    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    cnt = 0
    for i in range(n):
        for j in range(n):
            if normal_visited[i][j] == 0:
                current_alpha = rgb[i][j]
                normal_visited[i][j] = 1
                queue.append((i, j))
            else:
                continue
            while queue:
                cur_x, cur_y = queue.popleft()

                for c in range(4):
                    nx = cur_x + dx[c]
                    ny = cur_y + dy[c]

                    if nx < 0 or nx >= n or ny < 0 or ny >= n:
                        continue
                    if rgb[nx][ny] != current_alpha or normal_visited[nx][ny] == 1:
                        continue
                    normal_visited[nx][ny] = 1
                    queue.append((nx, ny))
            cnt += 1
    return cnt


def abnormal_bfs():
    queue = deque()

    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    cnt = 0
    for i in range(n):
        for j in range(n):
            if abnormal_visited[i][j] == 0:
                current_alpha = rgb[i][j]
                abnormal_visited[i][j] = 1
                queue.append((i, j))
            else:
                continue
            while queue:
                cur_x, cur_y = queue.popleft()

                for c in range(4):
                    nx = cur_x + dx[c]
                    ny = cur_y + dy[c]

                    if nx < 0 or nx >= n or ny < 0 or ny >= n:
                        continue
                    if abnormal_visited[nx][ny] == 1:
                        continue
                    if rgb[nx][ny] != current_alpha:
                        if (current_alpha == "R" or current_alpha == "G") and (rgb[nx][ny] == "R" or rgb[nx][ny] == "G"):
                            pass
                        else:
                            continue
                    abnormal_visited[nx][ny] = 1
                    queue.append((nx, ny))
            cnt += 1
    return cnt


n = int(input())
rgb = []
for _ in range(n):
    rgb.append(list(input()))

normal_visited = [[0] * n for _ in range(n)]
abnormal_visited = [[0] * n for _ in range(n)]

print(bfs(), abnormal_bfs())