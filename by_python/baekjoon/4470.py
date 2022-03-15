n = int(input())

result = []
for _ in range(n):
    result.append(input())

for i, s in enumerate(result, start=1):
    print(f"{i}. {s}")