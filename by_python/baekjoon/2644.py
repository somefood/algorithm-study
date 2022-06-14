def dfs(pos, L):
    global result
    if arr[pos][b] == 1:
        return L + 1

    for i in range(1, n + 1):
        if arr[pos][i] == 0 or visited[pos] == 1:
            continue
        visited[pos] = 1
        result = dfs(i, L + 1)
        visited[pos] = 0
    return result


result = 0
n = int(input())
a, b = map(int, input().split())
m = int(input())

arr = [[0] * (n + 1) for _ in range(n + 1)]

for _ in range(m):
    i, j = map(int, input().split())
    arr[i][j] = 1
    arr[j][i] = 1

visited = [0] * (n + 1)
# for i in range(1, n + 1):
#     for j in range(1, n + 1):
#         print(arr[i][j], end=" ")
#     print()

v = dfs(a, 0)
print(v if v else -1)

"""
9
7 3
7
1 2
1 3
2 7
2 8
2 9
4 5
4 6
"""