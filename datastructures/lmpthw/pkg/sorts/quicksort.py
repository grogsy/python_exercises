'''quick sort algorithm implemented to work with the double linked list datastructure made in learn more python the hard way'''

def quicksort(arr):
    # This is a helper function to run quicksort by
    # only taking the array to be sorted as argument.
    # This helps the user so they don't have to specify the initial low and high values
    _quicksort(arr, 0, arr.count-1)
    return arr


def _quicksort(arr, low, high):
    if low < high:
        splitpoint = partition(arr, low, high)

        # Scan the lower half of the partition
        _quicksort(arr, low, splitpoint-1)
        # Then scan the upper half
        _quicksort(arr, splitpoint+1, high)


def partition(arr, low, high):
    # arr.get(index) --> returns the value of arr at position of index
    node = arr.head

    i = 0
    while i < low:
        # scan up to the lowest position of the partition
        node = node.next
        i += 1
    lower_node = node

    j = i
    while j < high:
        # scan up to the highest position of the partition
        node = node.next
        j += 1
    pivot_node  = node
    pivot_value = pivot_node.value

    # begin swapping at lower_node up to the pivot_node
    node = lower_node

    while node is not pivot_node:
        if node.value < pivot_value:
            lower_node.value, node.value = node.value, lower_node.value
            lower_node = lower_node.next

            # incrementing i is necessary because it indicates the splitpoint position
            # of the next partition call
            i += 1

        node = node.next

    lower_node.value, node.value = node.value, lower_node.value

    return i
