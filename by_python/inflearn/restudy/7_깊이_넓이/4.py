def dfs(L, total):
    global cnt
    if total > t:
        return

    if L == k:
        if total == t:
            cnt += 1
        return

    for i in range(ns[L] + 1):
        dfs(L + 1, total + (ps[L] * i))


cnt = 0
t = int(input())
k = int(input())
ps = []
ns = []
for _ in range(k):
    p, n = map(int, input().split())
    ps.append(p)
    ns.append(n)

dfs(0, 0)
print(cnt)

"""
20
3
5 3
10 2
1 5
"""