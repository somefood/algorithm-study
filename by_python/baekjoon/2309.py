"""
브루트포스를 활용하자
"""

arr = [int(input()) for i in range(9)]

total = sum(arr)

for i in range(9):
    for j in range(i + 1, 9):
        if 100 == total - (arr[i] + arr[j]):
            num1, num2 = arr[i], arr[j]

            arr.remove(num1)
            arr.remove(num2)
            arr.sort()  # 오름차순 정리

            for k in range(len(arr)):
                print(arr[k])
            break

    if len(arr) < 9:
        break
