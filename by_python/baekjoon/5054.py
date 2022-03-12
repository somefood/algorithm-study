t = int(input())

for _ in range(t):
    n = int(input())
    pos = list(map(int, input().split()))
    pos.sort()
    sum = 0
    for i in range(1, len(pos)):
        sum += pos[i] - pos[i-1]
    print(sum * 2)