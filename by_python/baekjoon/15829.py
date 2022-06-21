L = int(input())
word = input()

total = 0
for i in range(len(word)):
    r = 31 ** i
    idx = ord(word[i]) - 96
    total += idx * r

print(total % 1234567891)

"""
5
abcde
"""