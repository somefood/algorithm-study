"""
- 처리되지 않은 데이터를 하나씩 골라 적절한 위치에 삽입
- 선택 정렬보단 좀 더 효율적
- 그래도 O(N^2)
- 만약 리스트 데이터가 거의 정렬되어 있다면 최선의 경우 O(N)

- 첫 번째 데이터는 정렬되어있다 판단하고, 두번째 데이터부터해서 첫번째 데이터보다 작으면 왼쪽으로 옮겨줌 크면 오른쪽에 둠
"""

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(1, len(array)):
    for j in range(i, 0, -1):
        if array[j] < array[j - 1]:
            array[j], array[j - 1] = array[j - 1], array[j]
        else:
            break

print(array)