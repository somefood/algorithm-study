import sys


def dfs(L, hap):
    global res
    if L > res:
        return
    if hap == m:
        if L < res:
            res = L
    if hap > m:
        return

    for i in range(len(a)):
        dfs(L + 1, hap + a[i])


n = int(input())
a = list(map(int, input().split()))
m = int(input())
res = sys.maxsize
a.sort(reverse=True)
dfs(0, 0)
print(res)

"""
3
1 2 5
15
"""