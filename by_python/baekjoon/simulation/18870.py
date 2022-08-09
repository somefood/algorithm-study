from collections import defaultdict
import sys

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

dic = defaultdict(int)
result = []
count = 0
for i in sorted(arr):
    if i in dic:
        continue
    dic[i] = count
    count += 1

for i in range(len(arr)):
    result.append(dic[arr[i]])

print(*result)

"""
5
2 4 -10 4 -9
"""