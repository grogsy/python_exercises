def insertion_sort(arr):
    sentinel_node = arr.head.next
    while sentinel_node:
        node = sentinel_node
        while node.prev and node.prev.value > node.value:
            node.value, node.prev.value = node.prev.value, node.value
            node = node.prev
        sentinel_node = sentinel_node.next

    return arr
