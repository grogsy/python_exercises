def sort(arr):
    if arr.count == 1 or arr.count == 0:
        return
    swapped = True
    while swapped:
        swapped = False
        for node in arr:
            if node is arr.tail:
                break
            nxt = node.next
            if node.value > nxt.value:
                node.value, nxt.value = nxt.value, node.value
                swapped = True
