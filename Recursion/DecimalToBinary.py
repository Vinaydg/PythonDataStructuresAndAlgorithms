def dtob(num):
    if num < 0:
        return -1
    if num == 1 or num == 0:
        return num
    return num % 2 + 10 * dtob(num // 2)


print(dtob(10))
