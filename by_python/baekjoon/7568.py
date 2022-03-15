n = int(input())

big_guy = []
result = [1] * n

for _ in range(n):
    big_guy.append(tuple(map(int, input().split())))

for i in range(n):
    for j in range(n):
        if i == j:
            continue
        if big_guy[i][0] < big_guy[j][0] and big_guy[i][1] < big_guy[j][1]:
            result[i] += 1

print(" ".join(map(str, result)))