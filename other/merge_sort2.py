'''Another variation of merge sort done(for some reason by me)
   in a complicated access-by-index fashion
'''

def sort(arr):
    if len(arr) == 0 or len(arr) == 1:
        return arr
    elif len(arr) == 2:
        if arr[0] > arr[1]:
            arr[0], arr[1] = arr[1], arr[0]
        return arr
    else:
        pivot = arr[0]
        lower  = []
        higher = []
        equal  = [pivot]

        j = 0
        k = 0
        m = 0
        for i in range(1, len(arr)+1):
            if arr[i] < pivot:
                lower.insert(j, arr[i])
                j += 1
            elif arr[i] > pivot:
                higher.insert(k, arr[i])
                k += 1
            else:
                equal.insert(m, arr[i])
                m += 1

    lower = sort(lower)
    higher = sort(higher)

    res = []
    i = 0
    while i < len(lower):
        res.insert(i, lower[i])
        i += 1

    j = 0
    while j < len(equal):
        res.insert(i, equal[j])
        i += 1
        j += 1

    k = 0
    while k < len(higher):
        res.insert(i, higher[k])
        i += 1
        k += 1

    return res
