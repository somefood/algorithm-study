import sys


def digit_sum(x):
    return sum(map(int, list(x)))


n = int(input())
lst = input().split()

max_value = -sys.maxsize
which = 0
for idx, i in enumerate(lst):
    if max_value < digit_sum(i):
        which = idx

print(lst[which])
