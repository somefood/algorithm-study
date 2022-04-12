s = input()
stack = []

result = 0
for x in s:
    if x.isdecimal():
        stack.append(x)
    else:
        b = stack.pop()
        a = stack.pop()
        stack.append(eval(f"{a} {x} {b}"))

result = stack[-1]
print(result)


"""
▣ 입력예제 1
352+*9-
▣ 출력예제 1
12
"""