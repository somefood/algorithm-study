student = [1] * 30
result = []

for _ in range(28):
    student[int(input()) - 1] -= 1

for i in range(len(student)):
    if student[i] == 1:
        result.append(i + 1)

result.sort()
for i in result:
    print(i)
