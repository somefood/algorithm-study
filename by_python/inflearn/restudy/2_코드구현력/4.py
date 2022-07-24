n = int(input())
students = list(map(int, input().split()))
result = []
avg = round(sum(students) / n)

for student in students:
    result.append(student - avg)

min_value = min(result, key=lambda x: abs(x))

index = result.index(abs(min_value))
print(avg, index + 1)

"""
10
45 73 66 87 92 67 75 79 75 80
"""