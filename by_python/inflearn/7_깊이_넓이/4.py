def dfs(L, hap):
    global cnt

    if hap > t:
        return

    if L == k:
        if hap == t:
            cnt += 1
        return
    for i in range(n[L] + 1):
        dfs(L + 1, hap + (p[L] * i))


t = int(input())
k = int(input())

cnt = 0
p = list()
n = list()
for _ in range(k):
    a, b = map(int, input().split())
    p.append(a)
    n.append(b)

dfs(0, 0)
print(cnt)

"""
20
3
5 3
10 2
1 5
"""