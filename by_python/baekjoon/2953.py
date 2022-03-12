result = []
for _ in range(5):
    result.append(sum(map(int, input().split())))

max_index = result.index(max(result))
print(max_index + 1, result[max_index])