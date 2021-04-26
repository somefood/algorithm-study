def med3(a, b, c):
    if (b >= a and c <= a) or (b <= a and c >= a):
        return a
    elif (a > b and c < b) or (a < b and c > b):
        return b
    return c


print(f"{med3(5, 4, 3)}")
print(f"{med3(1, 2, 3)}")