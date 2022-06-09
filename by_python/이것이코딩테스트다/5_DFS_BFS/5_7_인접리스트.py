# 행 ( R ow) 이 3 개인 2 차원 리스트로 인접 리스트 표현
graph = [[] for _ in range(3)]
# 노드 0 에 연결된 노드 정보 저장(노드, 거리)
graph[0].append((1, 7))
graph[0].append((2, 5))
# 노드 1 에 연결된 노드 징보 저장(노드 , 거리)
graph[1].append((0, 7))
# 노드 2 에 연결된 노드 정보 저장(노드, 거리)
graph[2].append((0, 5))
print(graph)
