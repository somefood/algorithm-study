t = int(input())

for _ in range(t):
    p, m = map(int, input().split())
    result = [i for i in range(1, m+1)]
    cnt = 0
    for i in range(p):
        hope = int(input())

        if hope in result:
            result.remove(hope)
        else:
            cnt += 1
    print(cnt)
