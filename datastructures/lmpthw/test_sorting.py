from random import choice
from pkg.structures.double_linked_list import DoubleLinkedList as Array

# Try to make all the sorting functions return a new object
# instead of modifying the existing one
def test_sort(sort_func):
    for _ in range(10):
        length = choice(range(10, 100))
        arr = Array()
        for _ in range(length):
            arr.push(choice(range(10000)))
        sorted_arr = sort_func(arr)
        for node in sorted_arr:
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
    from pkg.sorts.bubblesort import sort
    test_sort(sort)


def test_mergesort():
    from pkg.sorts.merge_sort import merge_sort
    test_sort(merge_sort)

test_bubblesort()
test_mergesort()
