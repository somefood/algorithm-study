def dfs(L):
    if L == m:
        print(*res)
        return

    for i in range(n):
        if visited[i] == 0:
            res[L] = arr[i]
            visited[i] = 1
            dfs(L + 1)
            visited[i] = 0


n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
res = [0] * m
visited = [0] * (n + 1)
dfs(0)

"""
4 2
9 8 7 1
"""