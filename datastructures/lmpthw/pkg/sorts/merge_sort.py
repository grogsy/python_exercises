'''
If it weren't for implementing an __iter__ method to the linked list,
I would've decided to implement Queues instead and iterating over them
would probably look something like this(also define an "empty" property
for linkedlists too):

    full_length = arr.count

    while not arr.empty:
        if arr.count > full_length//2:
            left.shift(arr.unshift())
        else:
            right.shift(arr.unshift())

In general though, I should remake the queue structure
so that it inherits from doublelinkedlist.

Summary of changes to make(This should be done after making the changes to Queue first):
    -Write a second merge_sort program that does not take advantage of __iter__ method I wrote.
     For the most part, that second program should be similar to this one anyway
    -Instead, try adapting the proposed change up there ^^^^
     in place of the for loop in this program
    -One major change here is save for the helper function defined,
     have the partitions(left and right) be instances of Queue instead of Array
'''
from ..structures.double_linked_list import DoubleLinkedList as Array
from ..structures.Queue import Queue

def merge_sort(arr):
    '''Helper function
       Need one because the result structure is a Queue which does not
       have its own __iter__ method(yet)
    '''
    q   = _merge_sort(arr)
    res = Array()

    while not q.empty:
        res.push(q.unshift())

    return res

def _merge_sort(arr):
    if arr.count <= 1:
        q = Queue()
        q.shift(arr.unshift())

        return q

    left  = Array()
    right = Array()

    midpoint = arr.count // 2

    # If you implement __iter__ for your structure
    # you support enumerate() also
    for i, node in enumerate(arr):
        if i < midpoint:
            left.push(node.value)
        else:
            right.push(node.value)

    left  = _merge_sort(left)
    right = _merge_sort(right)

    return merge(left, right)


def merge(left, right):
    res = Queue()

    while not left.empty and not right.empty:
        if left.head.value <= right.head.value:
            res.shift(left.unshift())
        else:
            res.shift(right.unshift())

    while not left.empty:
        res.shift(left.unshift())
    while not right.empty:
        res.shift(right.unshift())

    return res
