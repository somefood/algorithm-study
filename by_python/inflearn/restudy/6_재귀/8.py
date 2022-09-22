import sys

input = sys.stdin.readline


def dfs(L):
    global cnt
    if L == m:
        cnt += 1
        print(*result)
        return

    for i in range(1, n + 1):
        if visited[i] == 0:
            visited[i] = 1
            result[L] = i
            dfs(L + 1)
            visited[i] = 0


if __name__ == "__main__":
    n, m = map(int, input().split())
    result = [0] * m
    visited = [0] * (n + 1)
    cnt = 0
    dfs(0)
    print(cnt)


"""
3 2
"""