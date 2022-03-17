from sys import stdin

input = stdin.readline

i = 1
while True:
    split = input().split()
    if split[1] == "E":
        break
    else:
        c = " ".join(split)
        eval1 = eval(c)
        result = "true" if eval1 else "false"
        print(f"Case {i}: {result}")
        i += 1

