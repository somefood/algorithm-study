import sys

input = sys.stdin.readline


def dfs(cnt, total):
    global min_value
    if total > m:
        return

    if cnt > min_value:
        return

    if total == m:
        min_value = min(cnt, min_value)
        return

    for i in range(n):
        dfs(cnt + 1, total + arr[i])


if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort(reverse=True)
    m = int(input())
    min_value = sys.maxsize
    dfs(0, 0)
    print(min_value)


"""
3
1 2 5
15
"""