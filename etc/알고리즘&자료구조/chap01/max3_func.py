def max3(a, b, c):
    maximum = a
    if b > maximum: maximum = b
    if c > maximum: maximum = c
    return maximum


print(f'{max3(3, 2, 1)}')
print(f'{max3(1, 2, 3)}')
print(f'{max3(3, 10, 1)}')
