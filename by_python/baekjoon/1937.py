# TODO 다시 풀기

import sys

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)


def dfs(x, y):
    if dp[x][y] == 0:
        dp[x][y] = 1

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n and board[x][y] < board[nx][ny]:
                dp[x][y] = max(dp[x][y], dfs(nx, ny) + 1)

    return dp[x][y]


n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * n for _ in range(n)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
ans = 0


for i in range(n):
    for j in range(n):
        ans = max(ans, dfs(i, j))

print(ans)


for x in dp:
    print(x)

"""
4
14 9 12 10
1 11 5 4
7 15 2 13
6 3 16 8
"""