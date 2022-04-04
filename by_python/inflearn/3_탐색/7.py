n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]

res = 0
s = e = n // 2

sum1 = 0
# idx = 1
# for x in a:
#     sum1 += sum(x[s:e+1])
#
#     if s <= 0 and e >= 4:
#         idx *= -1
#
#     s -= idx
#     e += idx

for i in range(n):
    for j in range(s, e + 1):
        sum1 += a[i][j]
    if i < n // 2:
        s -= 1
        e += 1
    else:
        s += 1
        e -= 1

print(sum1)


"""
5
10 13 10 12 15
12 39 30 23 11
11 25 50 53 15
19 27 29 37 27
19 13 30 13 19

379
"""