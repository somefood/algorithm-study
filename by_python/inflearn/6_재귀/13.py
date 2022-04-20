def dfs(L):
    global path
    global cnt
    if L == n:
        print(path)
        cnt += 1
        return

    for i in range(1, n + 1):
        if g[L][i] == 0 or ch[i] == 1:
            continue
        ch[i] = 1
        path.append(i)
        dfs(i)
        path.pop()
        ch[i] = 0


if __name__ == "__main__":
    n, m = map(int, input().split())
    g = [[0] * (n + 1) for _ in range(n + 1)]
    ch = [0] * (n + 1)
    for i in range(m):
        a, b = map(int, input().split())
        g[a][b] = 1
    cnt = 0
    ch[1] = 1
    path = list()
    path.append(1)
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
