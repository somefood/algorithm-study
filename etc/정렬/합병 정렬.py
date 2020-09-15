def merge_sort(arr):
    if len(arr) < 2: print(arr, '요소가 하나네요'); return arr
    pivot = len(arr) // 2
    left = arr[0:pivot]
    right = arr[pivot:]
    print(f"1 mergesort {left} {right}")
    return merge(merge_sort(left), merge_sort(right))


def merge(left, right):
    print(f"2 merge {left} {right}")
    result = []
    while len(left) and len(right):
        if left[0] <= right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))

    while len(left): result.append(left.pop(0))
    while len(right): result.append(right.pop(0))
    print(3, result)
    return result


print(merge_sort([5, 2, 4, 7, 6, 1, 3, 8]))
