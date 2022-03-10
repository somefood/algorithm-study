school = int(input())

result = 0
for _ in range(school):
    student, apple = map(int, input().split())
    result += apple % student

print(result)
