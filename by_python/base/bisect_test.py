from bisect import bisect_left, bisect_right

arr = [9, 1, 2, 3, 4, 5, 2, 2, 8, 9, 3, 2, 2, 2, 2]


arr.sort()
print(bisect_left(arr, 2))
print(bisect_right(arr, 2))
print(arr)