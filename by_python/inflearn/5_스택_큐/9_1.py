a = input()
b = input()
sH = dict()

for x in a:
    sH = sH.get(x, 0) + 1

for x in b:
    sH = sH.get(x, 0) - 1

for x in a:
    if sH.get(x) != 0:
        print("NO")
        break
else:
    print("YES")

