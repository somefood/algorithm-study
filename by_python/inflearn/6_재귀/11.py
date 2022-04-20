def dfs(L, S):
    global cnt
    if L == k:
        if sum(res) % m == 0:
            print(*res)
            cnt += 1
        return
    for i in range(S, len(a)):
        if visited[i] == 0:
            visited[i] = 1
            res[L] = a[i]
            dfs(L + 1, i + 1)
            visited[i] = 0


cnt = 0
n, k = map(int, input().split())
a = list(map(int, input().split()))
visited = [0] * n
res = [0] * k
m = int(input())

dfs(0, 0)

print(cnt)
"""
5 3
2 4 5 8 12
6
"""