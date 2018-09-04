'''add two numbers respresented as linked lists
   restrictions: do not modify the linked lists
                 return value cannot be a linked list
                 solve by recursion
'''
def add(s1, s2, carry=False):
    '''
    input s1 --> Node (linked list head)
    input s2 --> Node (linked list head)

    returns -->  Node pointing to other nodes containing magnitudinal sums
    '''
    node1 = s1
    node2 = s2

    i = j = 0

    # Scan nodes to check if they're the same length or not
    while node1:
        node1 = node1.next
        i += 1

    while node2:
        node2 = node2.next
        j += 1

    # Calculate difference in length
    diff = abs(i-j)

    if diff == 0:
        # Same length, just recursive add and return early
        carry, node = recursive_add(s1, s2)
        if carry:
            node.prev = Node(1, prev=None, nxt=node)
            node = node.prev
        return node

    # Find which node is longer
    if i > j:
        greater = s1
        lesser  = s2
    else:
        greater = s2
        lesser  = s1

    k = 0
    # Copy longer node into a new Node until greater and lesser are same length(isn't this 'using explicit space' though? lol)
    greater_node = Node(greater.value, prev=None, nxt=None)
    greater      = greater.next
    k += 1

    while k < diff:
        greater_node.next = Node(greater.value, prev=greater_node, nxt=None)
        greater           = greater.next
        greater_node      = greater_node.next
        k += 1
    # End copying



    # Then recursive add
    carry, node = recursive_add(greater, lesser)

    # Link the greater node and the node carrying the recursive add
    greater_node.next = node
    node.prev         = greater

    carry, greater_node.value = divmod(greater.value+carry, 10)

    # Prepare the output node
    out_node = greater_node

    previous = greater_node.prev
    while previous and carry:
        # Performed for continuous carrying
        carry, previous.value = divmod(previous.value+carry, 10)

        out_node = previous
        previous = previous.prev

    if carry and not previous:
        out_node = Node(1, prev=None, nxt=out_node)
    elif previous and not carry:
        while previous:
            out_node = previous
            previous = previous.prev

    return out_node


def recursive_add(s1, s2):
    '''works when s1 and s2 are of same length'''
    if not s1.next and not s2.next:
        carry, s =  divmod(s1.value+s2.value, 10)
        return carry, Node(s, prev=None, nxt=None)

    carry, node = recursive_add(s1.next, s2.next)

    c, s = divmod(s1.value+s2.value, 10)

    s += carry

    prev_node = Node(s, prev=None, nxt=node)
    node.prev = prev_node

    return c, prev_node


def print_values(c):
    while c:
        print(c.value)
        c = c.next


class Node:
    def __init__(self, value, prev=None, nxt=None):
        self.value = value
        self.prev = prev
        self.next = nxt

