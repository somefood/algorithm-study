print('print *')
n = int(input())
w = int(input())

for i in range(n):
    print('*', end='')
    if i % w == w - 1:
        print()

if n % w:
    print()