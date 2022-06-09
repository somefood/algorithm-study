while True:
    v = int(input())

    if v == 0:
        break

    if str(v) == str(v)[::-1]:
        print("yes")
    else:
        print("no")

"""
121
1231
12421
0
"""