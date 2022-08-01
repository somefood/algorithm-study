import sys

n, s = map(int, input().split())
arr = list(map(int, input().split()))

interval_sum = 0
min_length = sys.maxsize
end = 0

for start, value in enumerate(arr):

    while 0 <= end < n and interval_sum < s:
        interval_sum += arr[end]
        end += 1

    if interval_sum >= s:
        min_length = min(min_length, (end - start))

    interval_sum -= value

print(min_length if min_length != sys.maxsize else 0)


"""
10 15
5 1 3 5 10 7 4 9 2 8
"""