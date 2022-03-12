t = int(input())

for _ in range(t):
    arr = list(map(int, input().split()))
    arr.sort()
    arr = arr[1:4]
    if arr[2] - arr[0] >= 4:
        print("KIN")
    else:
        print(sum(arr))
