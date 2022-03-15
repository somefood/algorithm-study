n = int(input())

result = []
for _ in range(n):
    result.append(tuple(map(int, input().split())))

result.sort(key=lambda x: (x[1], x[0]))

for x, y in result:
    print(x, y)