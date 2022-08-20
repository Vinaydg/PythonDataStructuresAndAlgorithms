def InsertionSort(arr):
    for i in range(1, len(arr)):
        ele = arr[i]
        for j in range(i - 1, -1, -1):
            if arr[j] > ele:
                arr[j + 1] = arr[j]
            if arr[j] <= ele:
                break
        arr[j + 1] = ele
    return arr


print(InsertionSort([1, 3, 2, 4]))
