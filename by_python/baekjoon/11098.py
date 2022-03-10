n = int(input())
for i in range(n):
    result = []
    p = int(input())
    for j in range(p):
        splits = input().split()
        c = int(splits[0])
        name = splits[1]
        result.append((c, name))
    result.sort(reverse=True, key=lambda x: x[0])
    print(result[0][1])