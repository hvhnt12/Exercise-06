# TASK1
def power(a, b):
    if a <= 0 or b <= 0:
        return -1
    elif b == 1:
        return a
    else:
        return a * power(a, b - 1)


# TASK2
def binary_search(numbers, num, left, right):
    if left > right:
        return -1

    mid = (left + right) // 2

    if numbers[mid] == num:
        return mid
    elif numbers[mid] > num:
        return binary_search(numbers, num, left, mid - 1)
    else:
        return binary_search(numbers, num, mid + 1, right)
