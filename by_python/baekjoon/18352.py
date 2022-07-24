from collections import deque
import sys

input = sys.stdin.readline

N, M, K, X = map(int, input().split())

cities = [[] for _ in range(N + 1)]
distance = [0] * (N + 1)
visited = [False] * (N + 1)
Q = deque()

# 간선 개수 만큼 반복
for _ in range(M):
    a, b = map(int, input().split())
    cities[a].append(b)

Q.append(X)
visited[X] = True
result = []
while Q:
    current = Q.popleft()

    for i in cities[current]:
        if not visited[i]:
            visited[i] = True
            Q.append(i)
            distance[i] = distance[current] + 1
            if distance[i] == K:
                result.append(i)

if len(result) == 0:
    print(-1)
else:
    result.sort()
    for i in result:
        print(i, end='\n')

"""
4 4 2 1
1 2
1 3
2 3
2 4

4 3 2 1
1 2
1 3
1 4
"""
