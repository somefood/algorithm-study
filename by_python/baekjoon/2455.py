import sys

max_people = -sys.maxsize

current = 0
for _ in range(4):
    o, i = map(int, input().split())
    current += i - o
    max_people = max(max_people, current)

print(max_people)

"""
0 32
3 13
28 25
39 0
"""