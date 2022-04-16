import sys


def DFS(L, sum):
    if sum > total // 2:
        return
    if L == n:
        if sum == total - sum:
            print("YES")
            sys.exit(0)  # 프로그램 전체 종료
    else:
        DFS(L + 1, sum + a[L])
        DFS(L + 1, sum)


if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))
    total = sum(a)
    DFS(0, 0)


"""
6
1 3 5 6 7 10 
"""