result = []
for i in range(9):
    num = int(input())
    result.append(num)

max_value = max(result)
print(max_value)
print(result.index(max_value)+1)