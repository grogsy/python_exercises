def reverse_list(node):
    if not node:
        return None
    prev = None
    curr = node
    nxt = node.next
    while nxt:
        curr.next = prev
        prev = curr
        curr = nxt
        nxt = curr.next

    curr.next = prev

    return curr