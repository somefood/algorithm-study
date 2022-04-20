def dfs(L, S):
    global cnt

    if L == m:
        print(*res)
        cnt += 1
        return

    for i in range(S, len(a)):
        if visited[i] == 0:
            visited[i] = 1
            res[L] = i
            dfs(L + 1, i + 1)
            visited[i] = 0


cnt = 0
n, m = map(int, input().split())
a = [i for i in range(n + 1)]
visited = [0] * (n+1)
res = [0] * m
dfs(0, 1)
print(cnt)

"""
4 2
"""