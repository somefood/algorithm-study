import math

n = int(input())
prime = [True] * (n + 1)
prime[0] = False
prime[1] = False

for i in range(2, int(math.sqrt(n)) + 1):
    for j in range(i + i, n + 1, i):
        prime[j] = False

print(prime.count(True))



"""
20
"""