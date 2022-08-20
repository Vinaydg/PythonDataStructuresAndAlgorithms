def BubbleSort(arr):
    count = 0
    for i in range(len(arr), 0, -1):
        noSwap = True
        for j in range(0, i-1):
            print(arr)
            count += 1
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                noSwap = False
            print(count)
        if noSwap:
            break
    return arr


print(BubbleSort([3,1,2,3,4]))
