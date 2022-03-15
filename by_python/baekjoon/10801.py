a = list(map(int, input().split()))
b = list(map(int, input().split()))

a_count = 0
b_count = 0

for i, j in zip(a, b):
    if i > j:
        a_count += 1
    elif i < j:
        b_count += 1

if a_count > b_count:
    print("A")
elif a_count < b_count:
    print("B")
else:
    print("D")