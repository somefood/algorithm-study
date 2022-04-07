from collections import deque

n, m = map(int, input().split())

weight = list(map(int, input().split()))
cnt = 0

weight.sort()
p = deque(weight)

while p:
    if len(p) == 1:
        cnt += 1
        break
    if p[0] + p[-1] > m:
        cnt += 1
        p.pop()
    else:
        p.pop()
        p.popleft()
        cnt += 1

# cur = 0
# left = 0
# right = n - 1
#
# while left <= right:
#     if weight[left] + weight[right] > m:
#         cnt += 1
#         right -= 1
#     else:
#         cnt += 1
#         left += 1
#         right -= 1

print(cnt)


"""
5 140
90 50 70 100 60
"""