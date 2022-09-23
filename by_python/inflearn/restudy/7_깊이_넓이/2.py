import sys


def dfs(L, pay):
    global max_value
    if L == n + 1:
        max_value = max(max_value, pay)
    else:
        if L + pt[L] <= n + 1:
            dfs(L + pt[L], pay + pp[L])
        dfs(L + 1, pay)


n = int(input())
pt = []
pp = []
max_value = -sys.maxsize
for _ in range(n):
    t, p = map(int, input().split())
    pt.append(t)
    pp.append(p)

pt.insert(0, 0)
pp.insert(0, 0)
dfs(1, 0)
print(max_value)

"""
7
4 20
2 10
3 15
3 20
2 30
2 20
1 10
"""
