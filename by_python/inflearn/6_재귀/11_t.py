def dfs(l, s, hap):

    global cnt

    if l == k:
        if hap % m == 0:
            cnt += 1

    for i in range(s, n):
        dfs(l + 1, i + 1, hap + a[i])


if __name__ == "__main__":
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    m = int(input())

    cnt = 0
    dfs(0, 0, 0)
    print(cnt)