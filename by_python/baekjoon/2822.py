result = [int(input()) for _ in range(8)]

sort_list = list(sorted(result, reverse=True))

print(sum(sort_list[:5]))
result = list(sorted([result.index(sort_list[i]) + 1 for i in range(5)]))

for i in result:
    print(i, end=" ")