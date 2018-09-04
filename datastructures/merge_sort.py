def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    left  = []
    right = []

    midpoint = len(arr) // 2

    for i, element in enumerate(arr):
        if i < midpoint:
            left.append(element)
        else:
            right.append(element)

    left  = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)


def merge(left, right):
    res = []
    while left and right:
        if left[0] <= right[0]:
            res.append(left.pop(0))
        else:
            res.append(right.pop(0))

    remaining = left or right

    return res+remaining

if __name__ == '__main__':
    from random import choice

    a = [choice(range(50)) for _ in range(20)]
    print("Before: ", a)
    print("After:  ", merge_sort(a))
