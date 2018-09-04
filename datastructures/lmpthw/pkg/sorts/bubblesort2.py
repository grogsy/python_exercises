'''Bubblesort on a DoubleLinkedList but without taking advantage of __iter__ method I provided'''

def sort(arr):
    '''bubble sort'''
    
    if arr.count <= 1:
        return arr

    swapped = True
    while swapped:
        swapped = False

        node = arr.head.next

        while node:
            prev = node.prev
            if prev.value > node.value:
                node.value, prev.value = prev.value, node.value
                swapped = True

            node = node.next

    return arr
