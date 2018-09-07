'''add two numbers respresented as linked lists
   restrictions: do not modify the linked lists
                 return value cannot be a linked list
                 solve by recursion
'''
class Node:
    def __init__(self, value, nxt=None):
        self.value = value
        self.next = nxt

    def __repr__(self):
        node = self
        res = ''

        while node:
            res += str(node.value)
            node = node.next

        return res


def recursive_add(n1, n2):
    if not n1.next and not n2.next:
        carry, _sum = divmod(n1.value + n2.value, 10)
        return carry, Node(_sum)

    carry, node = recursive_add(n1.next, n2.next)

    carry, _sum = divmod(n1.value + n2.value + carry, 10)

    return carry, Node(_sum, node)


def add(n1, n2):
    i = j = 0
    node1 = n1
    node2 = n2
    # Calculate length diff
    while node1:
        i += 1
        node1 = node1.next
    while node2:
        j += 1
        node2 = node2.next

    diff = abs(i-j)
    if not diff:
        carry, node = recursive_add(n1, n2)
        if carry:
            node = Node(1, node)
        return node

    if i > j:
        greater = n1
        lesser  = n2
    else:
        greater = n2
        lesser  = n1

    # add a buffer of 0's until lengths match up
    # Ex. 999 --->  999
    #      +1 ---> +001
    k = 1
    head = Node(0)
    n = head
    while k < diff:
        k+=1
        n.next = Node(0)
        n = n.next

    n.next = lesser
    lesser = head

    carry, node = recursive_add(greater, lesser)

    if carry:
     node = Node(1, node)

    return node

