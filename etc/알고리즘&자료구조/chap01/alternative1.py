n = int(input())

for i in range(n):
    if i % 2:
        print('-', end='')
    else:
        print('+', end='')

print()