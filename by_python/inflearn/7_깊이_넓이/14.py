import sys

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

sys.setrecursionlimit(10**6)


def dfs(x, y, h):
    ch[x][y] = 1
    for i in range(4):
        xx = x + dx[i]
        yy = y + dy[i]
        if 0 <= xx < n and 0 <= yy < n and ch[xx][yy] == 0 and board[xx][yy] > h:
            dfs(xx, yy, h)


if __name__ == "__main__":
    n = int(input())
    cnt = 0
    res = 0
    board = [list(map(int, input().split())) for _ in range(n)]
    for h in range(100):
        ch = [[0] * n for _ in range(n)]
        cnt = 0
        for i in range(n):
            for j in range(n):
                if ch[i][j] == 0 and board[i][j] > h:
                    cnt += 1
                    dfs(i, j, h)
        res = max(res, cnt)
        if cnt == 0:
            break

    print(res)

"""
5
6 8 2 6 2
3 2 3 4 6
6 7 3 3 2
7 2 5 3 6
8 9 5 2 7
"""