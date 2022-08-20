def binary_search(arr, val):
    beg = 0
    end = len(arr) - 1
    while beg <= end:
        middle = (beg + end) // 2
        if arr[middle] == val:
            return middle
        elif arr[middle] > val:
            end = middle - 1
        else:
            beg = middle + 1
    return -1


print(binary_search(["aab", "abcc", "val", "vin"], "vin"))
