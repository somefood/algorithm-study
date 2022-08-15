def dfs(L):
    if L == m:
        print(*res)
        return

    for i in range(1, n + 1):
        res[L] = i
        dfs(L + 1)


n, m = map(int, input().split())
res = [0] * m
dfs(0)
