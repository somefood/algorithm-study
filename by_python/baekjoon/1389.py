from collections import deque

n, m = map(int, input().split())

arr = [[0] * (n + 1) for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    arr[a][b] = 1
    arr[b][a] = 1

Q = deque()
kevin = [0] * n
for i in range(1, n + 1):
    visited = [-1] * (n + 1)
    visited[i] = 0
    for j in range(1, n + 1):
        if arr[i][j] == 0:
            continue
        visited[j] = visited[i] + 1
        Q.append(j)

        while Q:
            position = Q.popleft()

            for k in range(1, n + 1):
                if arr[position][k] == 0:
                    continue
                if visited[k] != -1:
                    visited[k] = min(visited[k], visited[position] + 1)
                    continue
                visited[k] = visited[position] + 1
                Q.append(k)
    kevin[i - 1] = sum(visited[1:])

print(kevin.index(min(kevin)) + 1)
# print(kevin.index(min(kevin)) + 1)

"""
5 5
1 3
1 4
4 5
4 3
3 2

5 7
1 2
1 3
2 3
2 4
3 4
3 5
4 5

6 8
1 3
5 2
6 3
4 5
3 1
4 1
5 4
2 6
"""