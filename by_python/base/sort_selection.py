"""
- 돌면서 제일 작은 원소를 찾아 인덱스 바꿔줌
- 이중 반복문 사용해야함
- O(N^2), N + (N - 1) + (N - 2) + .... + 2 -> (N^2 + N - 2)/2
"""

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(array)):
    min_index = i
    for j in range(i + 1, len(array)):
        if array[min_index] > array[j]:
            min_index = j
    array[i], array[min_index] = array[min_index], array[i]

print(array)