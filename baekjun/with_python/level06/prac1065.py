def hansu(n):
    han = 0
    if n < 100:
        return n
    for i in range(100, n + 1):
        li = [int(j) for j in str(i)]
        if li[1] - li[0] == li[2] - li[1]:
            han += 1
    return han + 99


n = int(input())
print(hansu(n))