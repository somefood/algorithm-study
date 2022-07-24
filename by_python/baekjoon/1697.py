from collections import deque


def bfs(n, k, step):
    Q = deque()
    visited = [0] * 100001
    Q.append((n, step))

    while Q:
        current, current_step = Q.popleft()

        if current == k:
            return current_step

        if current < 0 or current > 100000:
            continue
        if visited[current] == 1:
            continue

        visited[current] = 1
        Q.append((current - 1, current_step + 1))
        Q.append((current + 1, current_step + 1))
        Q.append((current * 2, current_step + 1))


if __name__ == "__main__":
    step = 0
    n, k = map(int, input().split())
    result = bfs(n, k, step)
    print(result)

