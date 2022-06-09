n, m = map(int, input().split())

arr = list(map(int, input().split()))

result = []
min_value = 99999999
for i in range(n - 2):
    for j in range(i + 1, n - 1):
        for k in range(j + 1, n):
            v = arr[i] + arr[j] + arr[k]
            result.append(m - v)


v = min(filter(lambda x: x >= 0, result))
print(m - v)
# print(min_value)

"""
5 21
5 6 7 8 9

10 500
93 181 245 214 315 36 185 138 216 295
"""