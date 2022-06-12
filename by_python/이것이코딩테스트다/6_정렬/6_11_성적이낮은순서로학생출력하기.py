n = int(input())

array = []
for i in range(n):
    input_data = input().split()
    array.append((input_data[0], int(input_data[1])))

array.sort(key=lambda x: x[1])

print(array)

"""
2
홍길동 95
이순신 77
"""