n = int(input())
arr = []
arr2 = []
for _ in range(n):
    data = input().split()
    arr.append((int(data[0]), data[1]))

arr.sort(key=lambda x: x[0])

for age, name in arr:
    print(age, name)

"""
3
21 Junkyu
21 Dohyun
20 Sunyoung
"""