n = int(input())

dic = {}
for _ in range(n):
    dic[input()] = False

for _ in range(n-1):
    s = input()
    dic[s] = True

for k, v in dic.items():
    if not v:
        print(k)
        break
