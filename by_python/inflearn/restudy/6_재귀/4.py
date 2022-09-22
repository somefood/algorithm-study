import sys

input = sys.stdin.readline


# def dfs(L):
#     global flag
#     if L == n:
#         sum1 = 0
#         sum2 = 0
#         for i in range(n):
#             if ch[i] == 1:
#                 sum1 += arr[i]
#             else:
#                 sum2 += arr[i]
#         if sum1 == sum2:
#             flag = True
#     else:
#         ch[L] = 1
#         dfs(L + 1)
#         ch[L] = 0
#         dfs(L + 1)
def dfs(L, total):
    if total > result // 2:
        return
    if L == n:
        if total == result - total:
            print("YES")
            sys.exit(0)
    else:
        dfs(L + 1, total + arr[L])
        dfs(L + 1, total)


if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))
    result = sum(arr)
    # ch = [0] * n
    # flag = False
    # dfs(0)
    # if flag:
    #     print("YES")
    # else:
    #     print("NO")
    dfs(0, 0)
    print("NO")

"""
6
1 3 5 6 7 10
"""