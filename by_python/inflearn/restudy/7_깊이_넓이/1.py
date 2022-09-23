import sys


def dfs(L, total, time):
    global max_value
    if time > m:
        return

    if L == n:
        max_value = max(max_value, total)
        return

    dfs(L + 1, total + arr[L][0], time + arr[L][1])
    dfs(L + 1, total, time)


n, m = map(int, input().split())
arr = []
visited = [0] * (n + 1)
max_value = -sys.maxsize
for _ in range(n):
    a, b = map(int, input().split())
    arr.append((a, b))

dfs(0, 0, 0)
print(max_value)

"""
5 20
10 5
25 12
15 8
6 3
7 4
"""