n = int(input())

for _ in range(n):
    split = input().split("-")

    first = split[0][::-1]
    second = int(split[1])
    result = 0
    for i in range(len(first)):
        result += (ord(first[i]) - 65) * (26 ** i)
    result = abs(result - second)

    if result <= 100:
        print("nice")
    else:
        print("not nice")
