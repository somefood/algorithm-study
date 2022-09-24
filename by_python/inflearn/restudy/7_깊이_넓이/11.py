import sys


def dfs(idx):
    global count

    if idx[0] == max_index[0] and idx[1] == max_index[1]:
        count += 1
        return

    cur_x = idx[0]
    cur_y = idx[1]
    for i in range(4):
        x = cur_x + dx[i]
        y = cur_y + dy[i]

        if x < 0 or x >= n or y < 0 or y >= n:
            continue
        if graph[cur_x][cur_y] >= graph[x][y] or visited[x][y] == 1:
            continue

        visited[x][y] = 1
        dfs((x, y))
        visited[x][y] = 0


n = int(input())

graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * n for _ in range(n)]
max_value = 0
min_value = sys.maxsize
min_index = 0
max_index = 0
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

for i in range(n):
    for j in range(n):
        if graph[i][j] > max_value:
            max_value = graph[i][j]
            max_index = (i, j)
        if graph[i][j] < min_value:
            min_value = graph[i][j]
            min_index = (i, j)

count = 0
dfs(min_index)
print(count)

"""
5
2 23 92 78 93
59 50 48 90 80
30 53 70 75 96
94 91 82 89 93
97 98 95 96 100
"""