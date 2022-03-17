n = int(input())

result = []
for _ in range(n):
    result.append(input())

result2 = list(result[0])

for word in result[1:]:
    for i in range(len(word)):
        if result2[i] == word[i]:
            continue
        else:
            result2[i] = "?"

print("".join(result2))