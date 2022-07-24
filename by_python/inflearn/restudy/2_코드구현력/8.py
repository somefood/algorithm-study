def reverse(x):
    reversed_list = list(reversed(x))
    return int("".join(reversed_list))


def reverse2(x):
    res = 0
    while x > 0:
        t = x % 10
        res = res * 10 + t
        x = x // 10
        print(t, res, x)
    return res


def isPrime(x):
    for i in range(2, x):
        if x % i == 0:
            return False
    return True


n = int(input())
lst = input().split()

prime = []
for l in lst:
    value = reverse(l)
    if isPrime(value):
        prime.append(value)

print(*prime)

"""
5
32 55 62 3700 250
"""
