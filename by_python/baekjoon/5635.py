n = int(input())

result = []
for _ in range(n):
    splits = input().split()
    name, day, month, year = splits[0], *map(int, splits[1:])
    result.append((name, day, month, year))

result.sort(key=lambda x: (x[3], x[2], [1]), reverse=True)
print(result[0][0])
result.sort(key=lambda x: (x[3], x[2], [1]))
print(result[0][0])