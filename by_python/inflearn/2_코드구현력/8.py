def reverse(x):
    v = list(reversed(list(x)))
    v = int("".join(v))
    return v


def is_prime(x):
    for i in range(2, x):
        if x % i == 0:
            return False
    return True


result = []
n = int(input())
lst = input().split()

for i in lst:
    rev = reverse(i)
    if is_prime(rev):
        result.append(rev)

print(result)