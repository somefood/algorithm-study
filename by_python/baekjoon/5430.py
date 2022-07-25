import sys
from collections import deque


def convert_to_deque(string: str) -> deque:
    string = string[1:-1]
    if len(string) == 0:
        return deque()
    return deque(map(int, string.split(",")))


def main():
    p = deque(sys.stdin.readline().rstrip())
    n = int(sys.stdin.readline().rstrip())
    arr = convert_to_deque(sys.stdin.readline().rstrip())

    if "R" not in p and len(arr) <= 0:
        return "error"

    count = 0
    for command in p:

        if command == "R":
            count += 1
        elif command == "D":
            if len(arr) <= 0:
                return "error"
            if count % 2 == 1:
                arr.pop()
            else:
                arr.popleft()

    if count % 2 == 0:
        return "[" + ",".join(map(str, arr)) + "]"
    else:
        arr.reverse()
        return "[" + ",".join(map(str, arr)) + "]"


t = int(input())

for _ in range(t):
    print(main())



"""
4
RDD
4
[1,2,3,4]
DD
1
[42]
RRD
6
[1,1,2,3,5,8]
D
0
[]
"""