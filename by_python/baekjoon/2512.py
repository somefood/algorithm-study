n = int(input())
arr = list(map(int, input().split()))
m = int(input())

start = 0
end = m
max_value = 0

while start <= end:
    mid = (start + end) // 2
    total = 0

    if sum(arr) <= m:
        max_value = max(arr)
        break

    for a in arr:
        if mid > a:
            total += a
        else:
            total += mid

    if total > m:
        end = mid - 1
    else:
        start = mid + 1
        max_value = max(max_value, mid)

print(max_value)

"""
4
120 110 140 150
485
"""