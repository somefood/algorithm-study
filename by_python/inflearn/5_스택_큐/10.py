import heapq

heap = []

while True:
    n = int(input())
    if n == -1:
        break
    elif n == 0:
        if len(heap) == 0:
            print(-1)
        else:
            print(heapq.heappop(heap))
    else:
        heapq.heappush(heap, n)

