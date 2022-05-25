def dfs(L):
    if dy[L] > 0:
        return dy[L]
    if L == 1 or L == 2:
        return L
    dy[L] = dfs(L - 1) + dfs(L - 2)


n = int(input())
dy = [0] * (n + 1)
print(dfs(n))