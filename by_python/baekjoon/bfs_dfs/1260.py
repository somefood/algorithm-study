from collections import deque


def dfs(v, L):
    if L == n:
        return

    for i in range(1, n + 1):
        if array[v][i] == 0 or dfs_visited[i] == 1:
            continue
        dfs_visited[i] = 1
        dfs_result.append(i)
        dfs(i, L + 1)


def bfs(v):
    queue = deque()
    queue.append(v)
    bfs_result.append(v)
    bfs_visited[v] = 1

    while queue:
        v = queue.popleft()
        for i in range(1, n + 1):
            if array[v][i] == 0 or bfs_visited[i] == 1:
                continue
            bfs_visited[i] = 1
            bfs_result.append(i)
            queue.append(i)


n, m, v = map(int, input().split())
array = [[0] * (n + 1) for i in range(n + 1)]
dfs_result = []
bfs_result = []
dfs_visited = [0] * (n + 1)
bfs_visited = [0] * (n + 1)

for _ in range(m):
    n1, n2 = map(int, input().split())
    array[n1][n2] = 1
    array[n2][n1] = 1

dfs_visited[v] = 1
dfs_result.append(v)

bfs(v)
dfs(v, 0)
print(" ".join(map(str, dfs_result)))
print(" ".join(map(str, bfs_result)))


"""
4 5 1
1 2
1 3
1 4
2 4
3 4

1 2 4 3
1 2 3 4
"""