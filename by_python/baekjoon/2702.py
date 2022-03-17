def gcd(a, b):
    a, b = max(a, b), min(a, b)
    result = 1
    while True:
        if a % b == 0:
            break
        a, b = b, a % b
    return b

n = int(input())

for _ in range(n):
    a, b = map(int, input().split())

    g = gcd(a, b)
    c = a * b // g
    print(c, g)