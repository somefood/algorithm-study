import collections

n, m = map(int, input().split())

result = [0] * (n + m + 1)

for i in range(1, n + 1):
    for j in range(1, m + 1):
        result[i + j] += 1

print(result)
max_value = max(result)

final = [i for i in range(len(result)) if result[i] == max_value]
print(final)