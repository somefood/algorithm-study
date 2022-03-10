T = int(input())

result = [map(int, input().split()) for i in range(T)]

for i, j in enumerate(result, 1):
    print(f"Case {i}: {sum(j)}")
