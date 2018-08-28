def sort(arr):
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
