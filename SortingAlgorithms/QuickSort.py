def pivot(left, right, arr):
    ele, index = arr[right], left
    for i in range(left, right):
        if arr[i] < ele:
            arr[i], arr[index] = arr[index], arr[i]
            index += 1
    arr[index], arr[right] = arr[right], arr[index]
    return index


def QuickSort(left, right, arr):
    if len(arr) <= 1:
        return arr
    if left < right:
        pi = pivot(left, right, arr)
        QuickSort(left, pi - 1, arr)
        QuickSort(pi + 1, right, arr)
    return arr


QuickSort(0, 8, [3, 3094, 349, 3489, 262, 262, 2739494, 45, 7])
