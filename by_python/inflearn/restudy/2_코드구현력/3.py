n, K = map(int, input().split())
input_array = list(map(int, input().split()))

result = []
for i in range(n - 2):
    for j in range(i + 1, n - 1):
        for k in range(j + 1, n):
            result.append(input_array[i] + input_array[j] + input_array[k])

result.sort(reverse=True)
idx = 1
first = result[0]
for i in range(1, len(result)):
    if first != result[i]:
        first = result[i]
        idx += 1

    if idx == K:
        print(result[i])
        break

"""
10 3
13 15 34 23 45 65 33 11 26 42
"""