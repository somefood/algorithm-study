n = int(input())


result = []
for i in range(n):
    total = i

    for each in str(i):
        total += int(each)

    if total == n:
        result.append(i)

if result:
    print(min(result))
else:
    print(0)

"""
216
"""