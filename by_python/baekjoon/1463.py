import sys

# 시간 초과..
def dfs(num, L):
    global min_count
    if num == 1:
        min_count = min(min_count, L)
        return

    if n % 3 == 0:
        dfs(num // 3, L + 1)
    if n % 2 == 0:
        dfs(num // 2, L + 1)
    dfs(num - 1, L + 1)


n = int(input())
# min_count = sys.maxsize
# dfs(n, 0)
# print(min_count)

arr = [0] * (n + 1)
for i in range(2, n + 1):
    arr[i] = arr[i - 1] + 1
    if i % 3 == 0:
        arr[i] = min(arr[i], arr[i // 3] + 1)
    if i % 2 == 0:
        arr[i] = min(arr[i], arr[i // 2] + 1)

print(arr[n])