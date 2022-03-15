from sys import stdin

input = stdin.readline

n = int(input())

a_count = 0
b_count = 0
for _ in range(n):
    a, b = map(int, input().split())

    if a > b:
        a_count += 1
    elif a < b:
        b_count += 1

print(a_count, b_count)