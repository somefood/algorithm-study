n = int(input())

result = list(set(map(int, input().split())))

result.sort()

print(" ".join(map(str,result)))

