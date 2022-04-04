import math

n = int(input())

result = [True] * (n + 1)

for i in range(2, int(math.sqrt(n))):
    result[i] = True
    for j in range(i + i, n + 1, i):
        result[j] = False

print(result.count(True) - 2)
