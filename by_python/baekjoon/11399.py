import heapq
import sys
from itertools import permutations


def dfs(L):
    if L == n:
        print(dfs_result)
        return

    for i in range(n):
        if visited[i] == 1:
            continue
        dfs_result[L] = people[i]
        visited[i] = 1
        dfs(L + 1)
        visited[i] = 0


n = int(input())
people = list(map(int, input().split()))
dfs_result = [0] * n
visited = [0] * n
dfs(0)


people.sort()
result = [0] * n
result[0] = people[0]
for i in range(1, n):
    result[i] = result[i-1] + people[i]

print(sum(result))

# min_value = sys.maxsize
# for p in permutations(people, n):
#     result = [0] * n
#     result[0] = p[0]
#     for i in range(1, n):
#         result[i] = result[i-1] + p[i]
#     min_value = min(min_value, sum(result))

# print(min_value)

"""
5
3 1 4 3 2
"""
