import sys

input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))

start = 0
end = max(arr)

result = 0
while start <= end:
    mid = (start + end) // 2

    temp_total = 0
    for tree in arr:
        if tree - mid > 0:
            temp_total += tree - mid
        if temp_total > m:
            break

    if temp_total >= m:
        start = mid + 1
        result = max(result, mid)
    else:
        end = mid - 1


print(result)
# print(max(result))

"""
4 7
20 15 10 17

5 20
4 42 40 26 46
"""