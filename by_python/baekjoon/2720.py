t = int(input())

coin = [25, 10, 5, 1]

for _ in range(t):
    count = 0
    money = int(input())
    result = []
    for c in coin:
        result.append(money // c)
        money = money % c

    print(" ".join(map(str, result)))
