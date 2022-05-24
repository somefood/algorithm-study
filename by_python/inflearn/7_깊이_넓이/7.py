from collections import deque


def bfs(v):
    queue = deque()
    queue.append(v)
    visited[v] = 0

    while queue:
        cur = queue.popleft()

        # if cur == e:
        #     return visited[cur]

        for i in [-1, 1, 5]:
            pos = cur + i

            if pos < 0 or pos > max_value:
                continue
            if visited[pos] != -1:
                continue

            visited[pos] = visited[cur] + 1
            if pos == e:
                return visited[pos]
            queue.append(pos)


s, e = map(int, input().split())
max_value = max(s, e)
dis = [i for i in range(max_value + 1)]
visited = [-1] * (max_value + 1)
print(bfs(s))

"5 14"