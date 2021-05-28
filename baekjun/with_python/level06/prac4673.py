# def d(n):
#     li = list(map(int, [i for i in str(n)]))
#     print(n + sum(li))


# d(1)

def func1(n):
    sum = 0
    for i in range(1, n+1):
        if i % 3 == 0 or i % 5 == 0:
            sum += i
    return sum

print(func1(16))
print(func1(34567))
print(func1(27639))