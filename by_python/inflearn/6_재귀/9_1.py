import itertools as it

n, f = map(int, input().split())
b = [1] * n

for i in range(1, n):
    b[i] = b[i-1]*(n-i)/i
a = list(range(1, n + 1))

for temp in it.permutations(a):
    sum = 0
    for l, x in enumerate(temp):
        sum += (b[l] * x)
    if sum == f:
        for x in temp:
            print(x, end=" ")
        break

"""
4 16
"""