def change(lst, idx, val):
    lst[idx] = val


x = [11, 22, 33, 44, 55]
print('x =', x)

index = int(input('업데이트할 인덱스 선택'))
value = int(input('새로운 값 입력'))

change(x, index, value)
print(x)