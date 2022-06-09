import math

a, b = map(int, input().split())
result = [True] * (b + 1)
result[0] = False
result[1] = False

for i in range(2, int(math.sqrt(b)) + 1):
    for j in range(i + i, b + 1, i):
        result[j] = False

for i in range(a, b + 1):
    if result[i]:
        print(i)








"""
3 16
"""