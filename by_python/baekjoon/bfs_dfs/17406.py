# TODO 다시 풀기

import sys
from itertools import permutations
from copy import deepcopy

N, M, K = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(N)]
rcs = [list(map(int, input().split())) for _ in range(K)]

ans = sys.maxsize

# 1. 회전 순서 정하기 (최대 6!=720)
for p in permutations(rcs, K):
    # 2. 회전
    copy_a = deepcopy(a)  # 원본리스트 카피
    for r, c, s in p:
        r -= 1
        c -= 1
        for n in range(s, 0, -1):
            tmp = copy_a[r - n][c + n] # 행 마지막 수 보관
            copy_a[r - n][c - n + 1:c + n + 1] = copy_a[r - n][c - n:c + n]  # ->
            for row in range(r - n, r + n):  # ↑
                copy_a[row][c - n] = copy_a[row + 1][c - n]
            copy_a[r + n][c - n:c + n] = copy_a[r + n][c - n + 1:c + n + 1]  # <-
            for row in range(r + n, r - n, -1):  # ↓
                copy_a[row][c + n] = copy_a[row - 1][c + n]
            copy_a[r - n + 1][c + n] = tmp

    # 3. 각 행의 최소값 찾기
    for row in copy_a:
        ans = min(ans, sum(row))

print(ans)

"""
5 6 2
1 2 3 2 5 6
3 8 7 2 1 3
8 2 3 1 4 5
3 4 5 1 1 1
9 3 2 1 4 3
3 4 2
4 2 1
"""
