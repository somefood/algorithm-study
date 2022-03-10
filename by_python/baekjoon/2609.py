def GCD(a, b):
    if a % b == 0:
        return b
    return GCD(b, a % b)


M, N = map(int, input().split())

print(GCD(M, N))
print(M * N // GCD(M, N))