import sys


def dfs(L, t1, t2, t3):
    global min_value
    if L == n:
        if t1 != t2 and t1 != t3 and t2 != t3:
            largest = max(t1, t2, t3)
            smallest = min(t1, t2, t3)
            min_value = min(min_value, largest - smallest)
            return
    else:
        dfs(L + 1, t1 + arr[L], t2, t3)
        dfs(L + 1, t1, t2 + arr[L], t3)
        dfs(L + 1, t1, t2, t3 + arr[L])


min_value = sys.maxsize
n = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))

dfs(0, 0, 0, 0)
print(min_value)

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