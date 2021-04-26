n = int(input())
w = int(input())


for _ in range(n // w):
    print('*' * w)

rest = n % w
if rest:
    print('*' * rest)
