def dfs(cur_x, cur_y):
    global cnt

    if cur_x == n - 1 and cur_y == n - 1:
        for x in visited:
            print(x)
        print()
        cnt += 1
        return

    visited[cur_x][cur_y] = 1
    for i in range(4):
        x = cur_x + dx[i]
        y = cur_y + dy[i]

        if x < 0 or x >= n or y < 0 or y >= n:
            continue
        if visited[x][y] == 1 or array[x][y] == 1:
            continue

        visited[x][y] = 1
        dfs(x, y)
        visited[x][y] = 0


dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
cnt = 0
n = 7
array = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * 7 for _ in range(n)]
dfs(0, 0)
print(cnt)

"""
0 0 0 0 0 0 0
0 1 1 1 1 1 0
0 0 0 1 0 0 0
1 1 0 1 0 1 1
1 1 0 0 0 0 1
1 1 0 1 1 0 0
1 0 0 0 0 0 0
"""
