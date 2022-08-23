import random


def BubbleSort(arr):
    count = 0
    for i in range(len(arr), 0, -1):
        noSwap = True
        for j in range(0, i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                noSwap = False
        if noSwap:
            break
    return arr


print(BubbleSort([random.randint(111, 1000) for i in range(1000)]))
