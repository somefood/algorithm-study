def binary_search(array, target, start, end):
    if start > end:
        return None

    mid = (start + end) // 2

    if array[mid] == target:
        return mid

    elif array[mid] > target:
        return binary_search(array, target, start, mid - 1)
    else:
        return binary_search(array, target, mid + 1, end)


# n ( 원소의 개수)과 ta rg et( 찾고자 하는 문자열 )을 임력받기
n, target = list(map(int, input().split()))
# 전체 원소 입력받기
array = list(map(int, input().split()))
# 이 진 탐색 수행 결과 출력
result = binary_search(array, target, 0, n - 1)
if result is None:
    print(" 원소가 존재하지 않습니다")
else:
    print(result + 1)

"""
10 7
1 3 5 7 9 11 13 15 17 19
"""
