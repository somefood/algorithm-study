word = input()

result = ""

for w in word:
    if w in "CAMBRIDGE":
        continue
    result += w

print(result)