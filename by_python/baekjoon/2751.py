from sys import stdin

input = stdin.readline

n = int(input())
result = []
for _ in range(n):
    result.append(int(input()))

result.sort()
for i in result:
    print(i)
"""
5
5
4
3
2
1
"""