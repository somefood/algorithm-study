"""
- 모든 노드에서 다른 노드까지의 최단 경로를 모두 계산.
- 다익스트라랑 마찬가지로 단계별로 거쳐가는 노드를 기준으로 파악
    - 매 단계마다 방문하지 않은 노드 중에 최단 경로 찾는 계산은 필요하지 않음
- 2차원 테이블에 보관
- 다이나믹 프로그래밍에 속함 (3중 반복문 사용)
- O(n^3)
- Dab = min(Dab, Dak + Dkb) 식 사용
"""
import sys

input = sys.stdin.readline
INF = int(1e9)

n = int(input())
m = int(input())
graph = [[INF] * (n + 1) for _ in range(n + 1)]


for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b:
            graph[a][b] = 0

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a][b] = c

# k 거쳐가는 노드 설정
for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

for a in range(1, n + 1):
    for b in range(1, n + 1):
        if graph[a][b] == INF:
            print("INFINITY", end=" ")
        else:
            print(graph[a][b], end=" ")
    print()


"""
4
7
1 2 4
1 4 6
2 1 3
2 3 7
3 1 5
3 4 4
4 3 2
"""

