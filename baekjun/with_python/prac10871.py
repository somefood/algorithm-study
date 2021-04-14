N, X = map(int, input().split())
result = [i for i in map(int, input().split(" ")) if i < X]

for i in result:
    print(f"{i} ", end="")