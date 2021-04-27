import random
from max import max_of

num = int(input())
lo = int(input())
hi = int(input())

x = [None] * num

for i in range(num):
    x[i] = random.randint(lo, hi)

print(x)
print(max_of(x))