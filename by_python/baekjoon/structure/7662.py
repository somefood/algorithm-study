# TODO 다시 풀기

import sys
import heapq

input = sys.stdin.readline

test = int(input())
for _ in range(test):
    max_heap, min_heap = [], []
    visited = [False] * 1_000_001

    k = int(input())

    for key in range(k):
        op, value = input().split()
        value = int(value)

        if op == "I":
            heapq.heappush(min_heap, (value, key))
            heapq.heappush(max_heap, (-value, key))
            visited[key] = True

        elif op == "D":
            if value == 1:
                while max_heap and not visited[max_heap[0][1]]:
                    heapq.heappop(max_heap)
                if max_heap:
                    v, k = heapq.heappop(max_heap)
                    visited[k] = False
            else:
                while min_heap and not visited[min_heap[0][1]]:
                    heapq.heappop(min_heap)
                if min_heap:
                    v, k = heapq.heappop(min_heap)
                    visited[k] = False

    while max_heap and not visited[max_heap[0][1]]:
        heapq.heappop(max_heap)

    while min_heap and not visited[min_heap[0][1]]:
        heapq.heappop(min_heap)

    print(f"{-max_heap[0][0]} {min_heap[0][0]}" if max_heap and min_heap else "EMPTY")

"""
1
7
I 16
I -5643
D -1
D 1
D 1
I 123
D -1

1
9
I -45
I 653
D 1
I -642
I 45
I 97
D 1
D -1
I 333


2
7
I 16
I -5643
D -1
D 1
D 1
I 123
D -1
9
I -45
I 653
D 1
I -642
I 45
I 97
D 1
D -1
I 333
"""
