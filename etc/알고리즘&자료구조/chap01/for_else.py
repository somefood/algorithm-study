import random

n = int(input())

for _ in range(n):
    r = random.randint(10, 90)
    print(r, end=' ')
    if r == 13:
        print('break')
        break
else:
    print(f'print {n} random count')