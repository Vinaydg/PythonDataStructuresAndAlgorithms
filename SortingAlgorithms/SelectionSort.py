def SelectionSort(arr):
    for i in range(len(arr)):
        minValue = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[minValue]:
                minValue = j
        if i != minValue:
            print(arr, arr[i], arr[minValue])
            arr[i], arr[minValue] = arr[minValue], arr[i]
    return arr


print(SelectionSort([19, 44, 38, 5, 47, 15]))
