def dfs(x, y):
    visited[x][y] = 1
    if x == 0:
        print(y)
        return
    if y - 1 >= 0 and arr[x][y-1] == 1 and visited[x][y-1] == 0:
        dfs(x, y - 1)
    elif y + 1 < N and arr[x][y+1] == 1 and visited[x][y+1] == 0:
        dfs(x, y + 1)
    else:
        dfs(x - 1, y)

N = 10
dy = [-1, 1]
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * N for _ in range(N)]

for i in range(N):
    if arr[N-1][i] == 2:
        dfs(N-1, i)


"""
1 0 1 0 0 1 0 1 0 1
1 0 1 1 1 1 0 1 0 1
1 0 1 0 0 1 0 1 0 1
1 0 1 0 0 1 0 1 1 1
1 0 1 0 0 1 0 1 0 1
1 0 1 1 1 1 0 1 0 1
1 0 1 0 0 1 0 1 1 1
1 1 1 0 0 1 0 1 0 1
1 0 1 0 0 1 1 1 0 1
1 0 1 0 0 2 0 1 0 1
"""