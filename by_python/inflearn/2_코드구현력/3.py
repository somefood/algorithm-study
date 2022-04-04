n, t = map(int, input().split())

lst = list(map(int, input().split()))
result = []
for i in range(n - 2):
    for j in range(i + 1, n - 1):
        for k in range(j + 1, n):
            result.append(lst[i] + lst[j] + lst[k])

result = list(set(result))
result.sort(reverse=True)
print(result[t-1])