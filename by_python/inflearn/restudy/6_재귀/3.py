import sys

input = sys.stdin.readline


def dfs(v):
    if v == n + 1:
        for i in range(1, n + 1):
            if ch[i] == 1:
                print(i, end=" ")
        print()
    else:
        # 상태 트리 구현, 사용 한다 & 사용하지 않는다.
        ch[v] = 1
        dfs(v + 1)
        ch[v] = 0
        dfs(v + 1)


if __name__ == "__main__":
    n = int(input())
    ch = [0] * (n + 1 )
    dfs(1)
