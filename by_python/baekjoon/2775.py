def dfs(k, n):
    if k == 0:
        return n
    if n == 1:
        return 1

    return dfs(k, n - 1) + dfs(k-1, n)


N = 15

arr = [[0] * N for _ in range(N)]
for i in range(N):
    arr[0][i] = i + 1
    arr[i][0] = 1

for i in range(1, N):
    for j in range(1, N):
        try:
            arr[i][j] = arr[i][j-1] + arr[i-1][j]
        except:
            pass

t = int(input())

# for _ in range(t):
#     k = int(input())
#     n = int(input())
#     result = 0
#     print(arr[k][n-1])


for _ in range(t):
    k = int(input())
    n = int(input())
    result = 0
    print(dfs(k, n))

"""
2
1
3
2
3
"""