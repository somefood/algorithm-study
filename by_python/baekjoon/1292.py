a, b = map(int, input().split())

result = []
cnt = 1
for i in range(1, 1001):
    if len(result) > 1000:
        break
    for j in range(i):
        result.append(cnt)
    cnt += 1

print(sum(result[a - 1: b]))