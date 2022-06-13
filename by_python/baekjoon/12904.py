s = input()
t = input()

for i in range(len(t) - len(s)):
    if t[-1] == "B":
        t = t[0:-1]
        t = t[::-1]
    elif t[-1] == "A":
        t = t[0:-1]

print(1 if s == t else 0)