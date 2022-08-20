import random


def digit(number, d):
    return (number // 10 ** (d)) % 10


def digitCount(number):
    if number == 0:
        return 1
    return len(str(number))


def mostDigit(arr):
    count = 0
    for i in arr:
        v = digitCount(i)
        if v > count:
            count = v
    return count


def RadixSort(arr):
    n = mostDigit(arr)
    for k in range(n):
        digitsBucket = [[] for i in range(10)]
        for i in range(len(arr)):
            digitsBucket[digit(arr[i], k)].append(arr[i])
        arr = []
        for i in digitsBucket:
            arr.extend(i)
    return arr


print(RadixSort([random.randint(1, 1000000) for i in range(100000)]))
