'''hoare scheme quicksort on lmpthw DLL
   This scheme would take advantage of the fact that nodes have references to their previous nodes
'''

def quicksort(arr):
    _quicksort(arr, 0, arr.count-1)
    return arr


def _quicksort(arr, low, high):
    if low < high:
        splitpoint = partition(arr, low, high)

        _quicksort(arr, low, splitpoint-1)
        _quicksort(arr, splitpoint+1, high)


def partition(arr, low, high):
    node = arr.head

    # Scan the array to find the low and high positions of the working partition
    i = 0
    while i < low:
        node = node.next
        i += 1
    left_node = node
    left_mark = i

    while i < high:
        node = node.next
        i += 1
    pivot_node = node
    right_node = pivot_node.prev
    right_mark = i-1
    # Done scanning


    # Begin swapping nodes
    node = left_node
    done = False

    while not done:
        while left_mark <= right_mark and left_node.value <= pivot_node.value:
            left_mark += 1
            left_node = left_node.next

        while right_mark >= left_mark and right_node.value >= pivot_node.value:
            right_mark -= 1
            right_node = right_node.prev

        if right_mark < left_mark:
            pivot_node.value, left_node.value = left_node.value, pivot_node.value
            done = True
        else:
            left_node.value, right_node.value = right_node.value, left_node.value

    return left_mark
