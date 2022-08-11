"""
- 너비 우선 탐색, 그래프에서 가까운 노드부터 우선적으로 탐색하는 알고리즘
- 큐 자료구조를 사용
    1. 탐색 시작 노드를 큐에 삽입하고 방문 처리
    2. 큐에서 노드를 꺼낸 뒤에 해당 노드의 인접 노드 중에서 방문하지 않는 노드를 모두 큐에 삽입하고 방문 처리
    3. 2번 수행할 수 없을때까지 반복
"""
from collections import deque


def bfs(graph, v, visited):
    q = deque()
    visited[v] = True
    q.append(v)

    while q:
        node = q.popleft()
        print(node, end=" ")
        for i in graph[node]:
            if not visited[i]:
                visited[i] = True
                q.append(i)


# 그래프 그려주기
graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

# 방문 처리
visited = [False] * 9

bfs(graph, 1, visited)

"""
1 2 3 8 7 4 5 6 
"""