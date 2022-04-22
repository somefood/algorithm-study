import sys


def dfs(L):
    global res

    if L == n:
        max_value = max(money)
        min_value = min(money)
        diff = max_value - min_value
        if diff < res:
            tmp = set()
            for x in money:
                tmp.add(x)
            if len(tmp) == 3:
                res = diff
        return

    for i in range(3):
        money[i] += coin[L]
        dfs(L + 1)
        money[i] -= coin[L] # 다시 돌려주기


n = int(input())
coin = []
money = [0] * 3
res = sys.maxsize
for i in range(n):
    coin.append(int(input()))

dfs(0)
print(res)

"""
7
8
9
11
12
23
15
17
"""
