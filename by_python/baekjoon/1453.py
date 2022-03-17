n = int(input())
result = [0] * 100

lst = map(int, input().split())
cnt = 0

for l in lst:
    if result[l-1] == 0:
        result[l-1] += 1
    else:
        cnt += 1

print(cnt)