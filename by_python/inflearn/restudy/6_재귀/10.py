import sys

input = sys.stdin.readline


def dfs(L, S):
    if L == m:
        print(*result)
        return

    for i in range(S, n + 1):
        if visited[i] == 0:
            visited[i] = 1
            result[L] = i
            dfs(L + 1, i + 1)
            visited[i] = 0


if __name__ == "__main__":
    n, m = map(int, input().split())
    result = [0] * m
    visited = [0] * (n + 1)
    dfs(0, 1)

"""
4 2
"""