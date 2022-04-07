def count(len):
    cnt = 0
    for x in a:
        cnt += (x//len)
    return cnt


k, n = map(int, input().split())

a = [int(input()) for _ in range(k)]

left = 1
right = max(a)
res = 0

while left <= right:
    cnt = 0
    mid = (left + right) // 2
    if count(mid) >= n:
        res = mid
        left = mid + 1
    else:
        right = mid - 1

print(res)


"""
4 11
802
743
457
539
"""