S = sum(map(int, input().split()))
T = sum(map(int, input().split()))

if S >= T:
    print(S)
elif S < T:
    print(T)