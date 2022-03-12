n = int(input())

arr = list(map(int, input().split()))
a_max = max(arr)
a_min = min(arr)

print(a_min * a_max)