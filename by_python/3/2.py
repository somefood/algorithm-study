N, M, K = map(int, input().split())

ls = list(map(int, input().split()))

ls.sort(reverse=True)

print(ls)

sum = 0
cnt = 0
idx = 0
for i in range(M):
    sum += ls[idx]
    cnt += 1
    if K == cnt:
        idx = 1
        cnt = 0
        continue
    if idx > 0 and ls[idx-1] != ls[idx]:
        idx = 0
        cnt = 0

print(sum)

"""
5 8 3
2 4 5 4 6

5 7 2
3 4 3 4 3
"""