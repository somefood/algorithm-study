def insertion_sort(arr):
    temp = 0
    for i in range(1, len(arr)):
        temp = arr[i]
        for j in range((i-1), -1, -1):
            if arr[j] > temp:
                arr[j+1] = arr[j]
            else:
                continue
            arr[j] = temp
    return arr


print(insertion_sort([5, 6, 1, 2, 4, 3]))