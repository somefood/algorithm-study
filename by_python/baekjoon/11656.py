word = input()

result = []
for i in range(len(word)):
    result.append(word[:i])

print(result)