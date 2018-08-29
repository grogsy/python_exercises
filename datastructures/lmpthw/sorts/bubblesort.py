'''Bubblesort'''
def sort(arr):
    if arr.count == 1 or arr.count == 0:
        return
    swapped = True
    while swapped:
        swapped = False
        for node in arr:
            prev = node.prev
            try:
                if prev.value > node.value:
                    node.value, prev.value = prev.value, node.value
                    swapped = True
            except (TypeError, AttributeError):
                # The case of the head as it does not have a previous value to compare
                pass
