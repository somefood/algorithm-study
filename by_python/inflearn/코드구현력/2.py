t = int(input())

for t in range(t):
    n, s, e, k = map(int, input().split())
    lst = list(map(int, input().split()))
    lst = lst[s - 1:e]
    lst.sort()
    print("#%d %d" % (t, lst[k - 1]))
