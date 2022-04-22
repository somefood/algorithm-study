import sys


def dfs(L, sum, time):
    global res
    if time > m:
        return
    if L == n:
        if sum > res:
            res = sum
    else:
        dfs(L + 1, sum + pv[L], time + pt[L]) # 문제 품
        dfs(L + 1, sum, time) # 문제 안 품


n, m = map(int, input().split())
pv = list()
pt = list()

for i in range(n):
    a, b = map(int, input().split())
    pv.append(a)
    pt.append(b)

res = -sys.maxsize
dfs(0, 0, 0)
print(res)