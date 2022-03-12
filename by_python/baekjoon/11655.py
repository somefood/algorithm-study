string = input()

alpha = "abcdefghijklmnopqrstuvwxyz"
result = ""
for s in string:
    if s.isalpha():
        if s.isupper():
            low = s.lower()
            result += alpha[(alpha.index(low) + 13) % 26].upper()
        else:
            result += alpha[(alpha.index(s) + 13) % 26]
    else:
        result += s

print(result)


"""
Baekjoon Online Judge
"""