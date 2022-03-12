words = input()

result = ""
for word in words.split("-"):
    result += word[0]

print(result)

"""
Knuth-Morris-Pratt
"""