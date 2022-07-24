n = int(input())
result = []
for _ in range(n):
    dices = list(map(int, input().split()))
    dices.sort()
    a = dices[0]
    b = dices[1]
    c = dices[2]
    if a == b and b == c:
        result.append(10000 + (a * 1000))
    elif a == b and a == c:
        result.append(1000 + (a * 100))
    elif b == c:
        result.append(1000 + (b * 100))
    else:
        result.append(a * 100)

result.sort()
print(result[-1])

"""
3
3 3 6
2 2 2
6 2 5
"""