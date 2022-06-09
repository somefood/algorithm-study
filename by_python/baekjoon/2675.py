T = int(input())

for _ in range(T):
    count, word = input().split()
    count = int(count)
    result = ""
    for w in word:
        if w:
            result += w * count
    print(result)

"""
2
3 ABC
5 /HTP
"""