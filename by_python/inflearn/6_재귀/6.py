def DFS(L):
    global cnt
    if L == m:
        cnt += 1
        print(*res)
        return
    for i in range(1, n + 1):
        res[L] = i
        DFS(L + 1)


if __name__ == "__main__":
    n, m = map(int, input().split())
    res = [0] * m
    cnt = 0
    DFS(0)
    print(cnt)