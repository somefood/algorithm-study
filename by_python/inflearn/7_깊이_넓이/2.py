import sys


def dfs(L, sum):
    global res
    if L == n + 1:
        if sum > res:
            res = sum

    else:
        if L + pt[L] <= n + 1:
            dfs(L + pt[L], sum + pp[L])
        dfs(L + 1, sum)


n = int(input())
pt = [0]
pp = [0]

for i in range(n):
    a, b = map(int, input().split())
    pt.append(a)
    pp.append(b)

res = -sys.maxsize
dfs(1, 0)
print(res)

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