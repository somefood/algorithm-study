n, m = map(int, input().split())

result = dict()
for i in range(1, n + 1):
    for j in range(1, m + 1):
        if (i + j) not in result:
            result[i + j] = 1
        else:
            result[i + j] += 1

max_value = max(result.values())
answer = [k for k, v in result.items() if v == max_value]

print(*answer)

"""
4 6
"""