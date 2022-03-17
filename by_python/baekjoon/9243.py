n = int(input())
s1 = input()
s2 = input()

suc = True
for i in range(len(s1)):
    a = int(s1[i])
    b = int(s2[i])
    if n % 2 == 1:
        if a + b != 1:
            suc = False
            break
    else:
        if a - b != 0:
            suc = False
            break
if suc:
    print("Deletion succeeded")
else:
    print("Deletion failed")
