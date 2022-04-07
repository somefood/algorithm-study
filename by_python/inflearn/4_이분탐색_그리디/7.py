l = int(input())
box = list(map(int, input().split()))
m = int(input())

for i in range(m):
    box.sort(reverse=True)
    box[0] -= 1
    box[-1] += 1

box.sort(reverse=True)
print(box[0] - box[-1])