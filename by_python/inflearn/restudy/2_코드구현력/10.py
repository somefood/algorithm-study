n = int(input())
a = list(map(int, input().split()))
cnt = 0
result = 0
for i in range(n):
    if a[i] == 1:
        cnt = cnt + 1
        result = result + cnt
    else:
        cnt = 0

print(result)

"""
10
1 0 1 1 1 0 0 1 1 0
"""
