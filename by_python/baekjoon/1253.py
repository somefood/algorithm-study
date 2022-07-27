#TODO 다시

import sys

N = int(input())
arr = list(map(int, sys.stdin.readline().split()))
arr.sort()
ans = 0

for i in range(N):
    tmp = arr[:i] + arr[i + 1:]
    left, right = 0, len(tmp) - 1
    while left < right:
        t = tmp[left] + tmp[right]
        if t == arr[i]:
            ans += 1
            break
        if t < arr[i]:
            left += 1  # t 를 증가시켜야 하므로 left 증가
        else:
            right -= 1  # t 를 감소시켜야 하므로 right 감소
print(ans)

# import sys
# n = int(input())
# arr = list(map(int, sys.stdin.readline().split()))
# arr.sort()
# result = set()
# answer = 0
# for i in range(n-1):
#     for j in range(i + 1, n):
#         if arr[i] + arr[j] in arr and arr[i] + arr[j] not in result:
#             answer += 1
#
# print(answer)

"""
10
1 2 3 4 5 6 7 8 9 10
"""
