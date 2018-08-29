from random import choice
from structures.double_linked_list import DoubleLinkedList as Array


def test_sort(sort_func):
    for _ in range(10):
        length = choice(range(10, 100))
        arr = Array()
        for _ in range(length):
            arr.push(choice(range(10000)))
        sort_func(arr)
        for node in arr:
            nxt  = node.next
            prev = node.prev
            try:
                assert prev.value <= node.value <= nxt.value
            except (TypeError, AttributeError):
                try:
                    # Is it the head?
                    assert node.value <= nxt.value
                except (TypeError, AttributeError):
                    # Must be the tail
                    assert prev.value <= node.value



def test_bubblesort():
    from sorts.bubblesort import sort
    test_sort(sort)

test_bubblesort()
