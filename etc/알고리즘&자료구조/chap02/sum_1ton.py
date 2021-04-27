def sum_1ton(n):
    s = 0
    while n > 0:
        s += n
        n -= 1
    return s

x = int(input('input x: '))
print(f'1 to {x} sum={sum_1ton(x)}')