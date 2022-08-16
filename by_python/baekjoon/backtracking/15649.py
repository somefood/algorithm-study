def dfs(depth):
    if depth == M:
        for i in range(depth):
            print(result[i], end=" ")
        print()
        return

    for i in range(1, N + 1):
        if visited[i] == 1:
            continue
        visited[i] = 1
        result.append(i)
        dfs(depth + 1)
        visited[i] = 0
        result.pop()


N, M = map(int, input().split())
result = []
visited = [0] * (N + 1)
dfs(0)

"""
4 2

1 2
1 3
1 4
2 1
2 3
2 4
3 1
3 2
3 4
4 1
4 2
4 3
"""