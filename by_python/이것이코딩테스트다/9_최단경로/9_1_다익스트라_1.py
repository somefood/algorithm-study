import sys

input = sys.stdin.readline
INF = int(1e9)  # 무한을 의 미 하는 값으로 10 억을 설정
# 노드의 개수 , 간선 의 개 수를 임 력 받거
n, m = map(int, input().split())
# 서 작 노드 번호를 임력받 기
start = int(input())
# 각 노드에 연결되 어 있는 노드에 대 한 정보를 담는 리 스트를 만들기
graph = [[] for i in range(n + 1)]
# 방문한 적 이 있는지 체크하는 목적의 리스트를 만들 기
visited = [False] * (n + 1)
# 최단 거리 테이블을 모두 무한으로 초기화
distance = [INF] * (n + 1)
# 모든 간선 경보를 입력받 기
for _ in range(m):
    a, b, c = map(int, input().split())
    # a 번 노드에서 b 번 노드로 가는 비용이 C 라는 의미
    graph[a].append((b, c))


# 방문하지 않은 노드 중에서, 가장 최단 거리가 짧은 노드의 번호를 반환
def get_smallest_node():
    min_value = INF
    index = 0  # 가장 최단 거 리 가 짧은 노드( 인덱스 )
    for i in range(1, n + 1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = 1
    return index


def dijkstra(start):
    # 시작 노드에 대해서 초기화
    distance[start] = 0
    visited[start] = True
    for j in graph[start]:
        distance[j[0]] = j[1]
    # 시작 노드를 제외한 전체 n - 1 개의 노드에 대해 반복
    for i in range(n - 1):
        # 현재 최단 거리가 가장 짧은 노드를 꺼 내 서, 방문 처리
        now = get_smallest_node()
        visited[now] = True
        # 현 재 노드와 연결된 다른 노드를 확인
        for j in graph[now]:
            cost = distance[now] + j[1]
            # 현재 노드를 거쳐서 다른 노드로 이 동하는 거 리가 더 짧은 경우
            if cost < distance[j[0]]:
                distance[j[0]] = cost


# 다익스트라 알고리즘 수행
dijkstra(start)

# 모든 노드로 가기 위한 최단 거리를 출력
for i in range(1, n + 1):
    # 도달할 수 없는 경우 , 무한(INFINITY ) 이라고 출 력
    if distance[i] == INF:
        print("INFINITY")
# 도달할 수 있는 경우 거 리를 출력
    else:
        print(distance[i])
