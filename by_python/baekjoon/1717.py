import sys

sys.setrecursionlimit(10 ** 8)
input = sys.stdin.readline


# 재귀를 활용해서 최종 부모까지 찾기
def find_parent(parent, k):
    if k != parent[k]:
        parent[k] = find_parent(parent, parent[k])
    return parent[k]


# unionfind 찾아서 조합하는건데 작은 쪽으로 연결 시켜줌
def union_find(parent, x, y):
    x = find_parent(parent, x)
    y = find_parent(parent, y)
    if x < y:
        parent[y] = x
    else:
        parent[x] = y


n, m = map(int, input().split())
parent = [i for i in range(n + 1)]
for _ in range(m):
    z, a, b = map(int, input().split())
    if z == 0:
        union_find(parent, a, b)
    else:
        # 최종 같은 부모면 YES 아니면 NO
        if find_parent(parent, a) == find_parent(parent, b):
            print('YES')
        else:
            print('NO')
print(parent)

"""
7 8
0 1 3
1 1 7
0 7 6
1 7 1
0 3 7
0 4 2
0 1 1
1 1 1
"""
