from collections import deque

n, k = map(int, input().split())

Q = deque([i for i in range(1, n + 1)])
result = []

while Q:

    for i in range(k - 1):
        Q.append(Q.popleft())
    result.append(Q.popleft())

print("<", end='')
for i in range(len(result) - 1):
    print("%d, " % result[i], end='')
print(result[-1], end='')
print(">")

"""
7 3
"""
