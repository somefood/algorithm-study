import sys

n, m = map(int, input().split())
result = []
for _ in range(n):
    arr = list(map(int, input().split()))
    result.append(arr)

max_value = -sys.maxsize
for r in result:
    max_value = max(max_value, min(r))

print(max_value)

"""
3 3
3 1 2
4 1 4
2 2 2

2 4
7 3 1 8
3 3 3 4
"""