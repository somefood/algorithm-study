n = int(input())

result = []
for _ in range(n):
    dice = list(map(int, input().split()))
    dice.sort()

    if dice[0] == dice[1] and dice[1] == dice[2]:
        result.append(10000 + dice[0] * 1000)
    elif dice[0] == dice[1] and dice[0] != dice[2]:
        result.append(1000 + dice[0] * 100)
    else:
        result.append(dice[-1] * 100)

print(result)
