import sys

input = sys.stdin.readline


def find_parent(parent, k):
    if parent[k] != k:
        parent[k] = find_parent(parent, parent[k])
    return parent[k]


def union(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


n = int(input())
m = int(input())

parent = [i for i in range(n + 1)]
arr = list()
for _ in range(m):
    a, b, c = map(int, input().split())
    arr.append((c, a, b))

# 작은 수부터 유니온 파인드 하면 최소 신장 트리 검색 가능
arr.sort()

total = 0
for v in arr:
    c, a, b = v

    if find_parent(parent, a) != find_parent(parent, b):
        union(parent, a, b)
        total += c


print(total)


"""
6
9
1 2 5
1 3 4
2 3 2
2 4 7
3 4 6
3 5 11
4 5 3
4 6 8
5 6 8
"""