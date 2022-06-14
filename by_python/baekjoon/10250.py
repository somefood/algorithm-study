t = int(input())

for _ in range(t):
    h, w, p = map(int, input().split())
    x = (p // h) + 1
    y = p % h
    if p % h == 0:
        x = p // h
        y = h
    print(f"{y}{x:02}")

# for i in range(t):
#     h, w, n = map(int, input().split())
#     num = n // h + 1
#     floor = n % h
#     if n % h == 0:  # h의 배수이면,
#         num = n // h
#         floor = h
#     print(f'{floor * 100 + num}')

"""
2
6 12 10
30 50 72
"""