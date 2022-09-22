n, m = map(int, input().split())
arr = [[0] * (n + 1) for _ in range(n + 1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    arr[a][b] = c

for i in range(1, n + 1):
    for j in range(1, n + 1):
        print(arr[i][j], end=" ")
    print()


"""
6 9
1 2 7
1 3 4
2 1 2
2 3 5
2 5 5
3 4 5
4 2 2
4 5 5
6 4 5
"""