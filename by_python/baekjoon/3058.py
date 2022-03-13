t = int(input())

for _ in range(t):
    result = map(int, input().split())
    f = list(filter(lambda x: x % 2 == 0, result))
    print(sum(f), min(f))


