from collections import deque


def bfs():
    result = []
    visited = [[0] * n for _ in range(n)]
    Q = deque()
    for i in range(n):
        for j in range(n):
            count = 0
            if arr[i][j] == 1 and visited[i][j] == 0:
                count = 1
                visited[i][j] = 1
                Q.append((i, j))

                while Q:
                    x, y = Q.popleft()

                    for k in range(4):
                        nx = x + dx[k]
                        ny = y + dy[k]

                        if nx < 0 or nx >= n or ny < 0 or ny >= n:
                            continue
                        if arr[nx][ny] == 0 or visited[nx][ny] != 0:
                            continue
                        visited[nx][ny] = 1
                        Q.append((nx, ny))
                        count += 1
                result.append(count)

    return result


dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
n = int(input())
arr = [list(map(int, list(input()))) for _ in range(n)]
result = bfs()

print(len(result))
result.sort()
for x in result:
    print(x)



"""
7
0110100
0110101
1110101
0000111
0100000
0111110
0111000
"""