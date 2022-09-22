def dfs(L):
    global cnt
    if L == n:
        cnt += 1
        return

    for i in range(1, n + 1):
        if arr[L][i] == 1 and visited[L] == 0:
            visited[L] = 1
            dfs(i)
            visited[L] = 0


cnt = 0
n, m = map(int, input().split())
arr = [[0] * (n + 1) for _ in range(n + 1)]
visited = [0] * (n + 1)
for _ in range(m):
    a, b = map(int, input().split())
    arr[a][b] = 1

dfs(1)
print(cnt)

"""
5 9
1 2
1 3
1 4
2 1
2 3
2 5
3 4
4 2
4 5
"""