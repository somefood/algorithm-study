word = input()

result = ""

for w in word:
    if w.isupper():
        result += w.lower()
    else:
        result += w.upper()

print(result)