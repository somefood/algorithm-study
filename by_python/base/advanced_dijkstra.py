"""
우선 순위 큐를 도입하여 시간 복잡도 줄이기
    - 가장 높은 데이터를 가장 먼저 삭제하는 자료구 O(logN) <-> 리스트 삽입 O(1), 삭제 O(N)

파이썬은 최소 힙만 제공하기에 최대 힙 구현하려면 -부호 넣어서 처리해주기, pop때 다시 -처리

[다익스트라 진화]
단계마다 방문하지 않은 노드 중에서 최단 거리가 가장 짧은 노드를 선택함 (최소 힙 사용)
이렇게 하면 O(ElogE) -> or O(ElogV), while문은 V 이상으로 처리 되지 않음, 최대 간선 수 만큼만
간선이 1~20만개이거나, 노드 만 개 이상일 때 처리하기 좋다
"""
import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
start = int(input())
graph = [[] for i in range(n + 1)]
distance = [INF] * (n + 1)

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


dijkstra(start)


for i in range(1, n + 1):
    if distance[i] == INF:
        print("INFINITY")
    else:
        print(distance[i])

"""
6 11
1
1 2 2
1 3 5
1 4 1
2 3 3
2 4 2
3 2 3
3 6 5
4 3 3
4 5 1
5 3 1
5 6 2
"""