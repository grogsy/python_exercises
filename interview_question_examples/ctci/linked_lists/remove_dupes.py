# ctci 2.1

from linked_list import Node, print_nodes

def delete_dupes(node):
    '''with a data buffer(set)'''
    seen = set()
    prev = None
    while node is not None:
        if node.data in seen:
            prev.next = node.next
        else:
            seen.add(node.data)
            prev = node
        
        node = node.next

arr = [3, 2, 2, 2, 3, 1, 3, 1, 2 , 3]
head = Node(1)

for n in arr:
    head.append(n)

print_nodes(head)

delete_dupes(head)

print_nodes(head)
