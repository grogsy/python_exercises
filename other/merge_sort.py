def sort(arr):
    if len(arr) <= 1:
        return arr
    elif len(arr) == 2:
        if arr[0] > arr[1]:
            arr[0], arr[1] = arr[1], arr[0]
        return arr
    else:
        pivot = arr[0]
        lower = []
        higher = []
        equal = []
        for item in arr:
            if item < pivot:
                lower.append(item)
            elif item > pivot:
                higher.append(item)
            else:
                equal.append(item)

    return sort(lower)+sort(equal)+sort(higher)
