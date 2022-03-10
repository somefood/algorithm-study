N = int(input())

ox = list(map(int, input().split()))
result = [0 for i in range(N)]

cnt = 0
for i in range(N):
    if i <= 0:
        result[i] = ox[i]
        continue
    if ox[i] != 0:
        cnt = result[i-1]
        if ox[i-1] != 0:
            cnt += 1
        else:
            cnt = 1
    else:
        cnt = 0
    result[i] = cnt

hap = 0
result=0
for i in range(N):
    if ox[i] == 1:
        hap += 1
        result += hap
    else:
        hap = 0

# print(sum(result))
print(result)
"""
10
1 0 1 1 1 0 0 1 1 0
"""