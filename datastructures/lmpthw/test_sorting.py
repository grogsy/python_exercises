from structures.double_linked_list import DoubleLinkedList as Array
from random import choice


def test_bubblesort():
    from sorts.bubblesort import sort
    for _ in range(10):
        length = choice(range(10, 100))
        arr = Array()
        for _ in range(length):
            arr.push(choice(range(10000)))
        sort(arr)
        for node in arr:
            if node is arr.tail:
                break

            nxt = node.next
            if node is arr.head:
                assert node.value <= nxt.value
            else:
                prev = node.prev
                assert prev.value <= node.value <= nxt.value

test_bubblesort()

