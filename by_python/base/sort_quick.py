"""
- 기준 데이터를 설정하고 그 기준보다 큰 데이터와 작은 데이터의 위치를 바꿈
- 많이 사용되는 알고리즘 중 하나
- 병합 정렬과 더불어 정렬 라이브러리의 근간이 되는 알고리즘
- 첫 번째 데이터를 기준 데이터(Pivot)로 설정
- O(NlogN), 최악의 경우 O(N^2) -> 이미 정렬된 배열일때 퀵소트하면 해야허니..
- 기본 라이브러리 sort()는 O(NlogN) 보장

1. 피벗을 정하고, 왼쪽에서는 피벗보다 큰 값을, 오른쪽에서는 작은 값을 고르며 이 둘을 변경해줌
2. 1을 반복하다가 왼쪽, 오른쪽이 엇갈리는 경우 "피벗"과 "작은 데이터"의 위치를 바꿔줌
3. 바꿔주면 기피벗이었던 기준으로 왼쪽은 작은 데이터, 오른쪽은 큰 데이터로 정렬이 된 거임
4. 이를 분할해줘서 처리해주면
"""

array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]


def quick_sort(array, start, end):
    if start >= end:
        return
    pivot = start
    left = start + 1
    right = end

    while left <= right:
        while left <= end and array[left] <= array[pivot]:
            left += 1
        while right > start and array[right] >= array[pivot]:
            right -= 1

        # 엇갈리면 피벗하고 작은거하고 바꿔줌
        if left > right:
            array[right], array[pivot] = array[pivot], array[right],
        # 엇갈리지 않았다면 작은 데이터와 큰 데이터 교체
        else:
            array[left], array[right] = array[right], array[left],
    quick_sort(array, start, right - 1)
    quick_sort(array, right + 1, end)


def quick_sort_with_slicing(array):
    if len(array) <= 1:
        return array
    pivot = array[0]
    tail = array[1:]

    left_side = [x for x in tail if x <= pivot]
    right_side = [x for x in tail if x > pivot]

    return quick_sort_with_slicing(left_side) + [pivot] + quick_sort_with_slicing(right_side)


quick_sort(array, 0, len(array) - 1)
quick_sort_with_slicing(array)
print(array)