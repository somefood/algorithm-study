T = int(input())

for _ in range(T):
    result = []
    str1, str2 = input().split()
    for s1, s2 in zip(str1, str2):
        d1, d2 = ord(s1), ord(s2)
        if d2 >= d1:
            result.append(d2 - d1)
        else:
            result.append(d2 + 26 - d1)

    print("Distances:", *result)
