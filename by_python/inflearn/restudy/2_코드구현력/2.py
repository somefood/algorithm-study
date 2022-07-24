t = int(input())

for _ in range(t):
    n, s, e, k = map(int, input().split())
    input_array = list(map(int, input().split()))
    result = input_array[s:e+1]
    result.sort()
    print(result[k-1])


"""
1
6 2 5 3
5 2 7 3 8 9

2
6 2 5 3
5 2 7 3 8 9
15 3 10 3
4 15 8 16 6 6 17 3 10 11 18 7 14 7 15
"""