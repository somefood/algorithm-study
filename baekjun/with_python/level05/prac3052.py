result = []
for i in range(10):
    num = int(input())
    result.append(num%42)

print(len(set(result)))
