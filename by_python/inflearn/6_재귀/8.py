def dfs(depth):
    global cnt
    if depth == m:
        print(*result)
        cnt += 1
        return

    for i in range(1, len(a)):
        if visited[i]:
            continue
        result[depth] = a[i]
        visited[i] = True
        dfs(depth + 1)
        visited[i] = False


cnt = 0
n, m = map(int, input().split())
a = [i for i in range(n + 1)]
result = [0] * m
visited = [False] * (n + 1)
dfs(0)
print(cnt)