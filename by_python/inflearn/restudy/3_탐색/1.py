def is_palindrome(word):
    word = word.lower()
    return word == word[::-1]


n = int(input())
for _ in range(n):
    word = input()
    print("YES" if is_palindrome(word) else "NO")

"""
5
level
moon
abcba
soon
gooG
"""