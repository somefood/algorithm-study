n = int(input())

i = 0
count = 0
while True:
    i += 1
    if "666" in str(i):
        count += 1
    if count == n:
        print(i)
        break

"""
500

예제 출력 5
166699
"""