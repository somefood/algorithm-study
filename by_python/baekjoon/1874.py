n = int(input())
stack = []
result = []
idx = 1
flag = True

for _ in range(n):
    a = int(input())

    while idx <= a:
        stack.append(idx)
        result.append("+")
        idx += 1

    if stack[-1] == a:
        stack.pop()
        result.append("-")
    else:
        flag = False


if flag:
    for i in result:
        print(i)
else:
    print("NO")



"""
8
4
3
6
8
7
5
2
1

5
1
2
5
3
4
"""
