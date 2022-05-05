from collections import deque


def bfs():
    Q = deque()
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    Q.append((0, 0))
    visited[0][0] = 1

    while Q:
        cur_x, cur_y = Q.popleft()

        for i in range(4):
            x = cur_x + dx[i]
            y = cur_y + dy[i]

            if x < 0 or x >= n or y < 0 or y >= n:
                continue
            if visited[x][y] != 0 or array[x][y] == 1:
                continue

            visited[x][y] = visited[cur_x][cur_y] + 1
            Q.append((x, y))

    print(visited[n - 1][n - 1] - 1)


n = 7
array = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * 7 for _ in range(n)]
bfs()

"""
0 0 0 0 0 0 0
0 1 1 1 1 1 0
0 0 0 1 0 0 0
1 1 0 1 0 1 1
1 1 0 1 0 0 0
1 0 0 0 1 0 0
1 0 1 0 0 0 0
"""
