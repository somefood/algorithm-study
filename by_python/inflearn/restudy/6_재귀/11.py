import sys

input = sys.stdin.readline


def dfs(L, S):
    global cnt
    if L == k:
        total = sum(result)
        if total % m == 0:
            cnt += 1
        return

    for i in range(S, n):
        if visited[i] == 0:
            visited[i] = 1
            result[L] = arr[i]
            dfs(L + 1, i + 1)
            visited[i] = 0


if __name__ == "__main__":
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    m = int(input())
    cnt = 0
    result = [0] * k
    visited = [0] * (n + 1)
    dfs(0, 0)
    print(cnt)


"""
5 3
2 4 5 8 12
6
"""