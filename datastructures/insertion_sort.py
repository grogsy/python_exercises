def insertion_sort(arr):
    i = 0
    while i < len(arr):
        j = i
        while j > 0 and arr[j-1] > arr[j]:
            arr[j], arr[j-1] = arr[j-1], arr[j]
            j -= 1
        i += 1
