T = int(input())

for _ in range(T):
    N = int(input())
    print(sum(filter(lambda x: x <= 10, map(int, input().split()))))

