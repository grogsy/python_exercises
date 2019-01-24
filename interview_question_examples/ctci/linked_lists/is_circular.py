# ctci 2.8

def is_circular(linked_list):
    head = linked_list.head
    node = linked_list.head
    while node is not None:
        if node.next == head:
            return node.next.value
        node = node.next
    
