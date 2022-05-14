from collections import deque, defaultdict

computer = int(input())
e = int(input())

arr = [[0] * (computer + 1) for _ in range(computer + 1)]
graph = defaultdict(list)
visited = [0] * (computer + 1)

for i in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


Q = deque()
visited[1] = 1
Q.append(graph[1])
count = 0

while Q:
    now = Q.popleft()

    for n in now:
        if visited[n] != 0:
            continue
        count += 1
        visited[n] = 1
        Q.append(graph[n])

print(count)