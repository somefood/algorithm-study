T = int(input())

for i in range(T):
    price = int(input())
    N = int(input())
    for j in range(N):
        m = list(map(int, input().split()))
        price += m[0] * m[1]
    print(price)
